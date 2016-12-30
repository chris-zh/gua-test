var log = function(){
    console.log(arguments);
}
var vip = {}
vip.ajax = function(url, method, form, response){
    var request = {
        url: url,
        type: method,
        contentType: 'application/json',
        success: function(r){
            log('ajax', method, url, r);
            response(r);
        },
        error:function(err){
            log('err', err);
        }
    };
    if(method=='post'){
        request.data = JSON.stringify(form);
    }
    $.ajax(request);
}

var guaForm = function(button){
    var b = $(button);
    var inputs = b.closest('.gua-form').find('.gua-input');
    var form = {};
    $.each(inputs, function(index, input){
        log('input', input);
        let value = input.value;
        if(value!=''){
            let key = input.dataset.key;
            form[key] = value;
        }
    });
    return form;
}

var Guaction = function(button){
    var path = button.dataset.path;
    var method = button.dataset.method;
    var form = guaForm(button);
    var block = button.dataset.block;
    var response = window[block];
    vip.ajax(path, method, form, response);
}
