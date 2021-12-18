window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let t_href = event.target
        $.ajax(
            {
                url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",
                success: function (data) {
                    $('.basket_list').html(data.result)
                },
            });
        event.preventDefault()
    })

    $('.product_add_basket').on('click', 'button[type="button"]', function () {
        let t_href = event.target.value
        $.ajax(
            {
                url: "/basket/add/" + t_href + "/",
                success: function (data) {
                    $('.product_add_basket').html(data.result)
                },
            });
        event.preventDefault()
    })
}
