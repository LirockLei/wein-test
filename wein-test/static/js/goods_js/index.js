$(document).ready(function(){
    $.ajax({
        url: '/goods/show_all_goods/',
        dataType: 'json',
        type: 'GET',
        success: function(data){
            console.log(data)
            for(index in data.data){
                goods = data.data[index]
                if (data.code == '200'){
                    ulNode = $('.goods-module')

                    liNode = $('<li></li>')

                    div1Node = $('<div></div>').attr('class', 'goods')

                    div11Node = $('<div></div>').attr('class', 'image')

                    imgNode = $('<img/>').attr('src', goods.img_url)

                    div12Node = $('<div></div>').attr('class', 'goods-info')

                    span1Node = $('<span>' + goods.title +  '</span>').attr('id', 'goods-title')

                    brNode = $('<br/>')

                    span2Node = $('<span>' + goods.price  + '</span>').attr('id', 'goods-price')

                    span3Node = $('<span>' + goods.detail  + '</span>').attr('id', 'goods-detail')

                    buttonNode = $('<button class="del-button" type="button">删除此商品</button>').attr('goods-id', goods.id)

                    ulNode.append(liNode)
                    liNode.append(div1Node)
                    div1Node.append(div11Node)
                    div1Node.append(div12Node)
                    div11Node.append(imgNode)
                    div12Node.append(span1Node)
                    div12Node.append(brNode)
                    div12Node.append(span2Node)
                    div12Node.append(brNode)
                    div12Node.append(span3Node)
                    div12Node.append(brNode)
                    div12Node.append(buttonNode)
                }
            }
        },
        error: function(data){
            alert('error')
        }
    })
    $('.del-button').click(function(){
        var goods_id = $('.del-button').attr('goods-id')
        $.ajax({
            url: '/goods/del_goods/',
            type: 'DELETE',
            dataType: 'json',
            data: {'goods-id': goods_id},
            success: function(data){
                console.log(data)
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