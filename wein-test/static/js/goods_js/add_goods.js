$(document).ready(function(){
    $('.form-add').submit(function(e){
        e.preventDefault();
        $(this).ajaxSubmit({
            url: '/goods/add_goods/',
            type: 'POST',
            dataType: 'json',
            success: function(data){
                console.log(data)
                if(data.code == '601'){
                    $('#error-msg span').html(data.msg)
                    $('#error-msg').show()
                }
                if(data.code == '602'){
                    $('#error-msg span').html(data.msg)
                    $('#error-msg').show()
                }
                if(data.code == '200'){
                    location.href = '/goods/all_goods/'
                }
            },
            error: function(data){
                alert('error')
            }
        })
    })
})