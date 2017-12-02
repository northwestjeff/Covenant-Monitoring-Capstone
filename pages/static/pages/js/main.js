$(document).on("change", 'input[type="checkbox"]', function () {
    // console.log($(this));
    //     var isChecked = $(this).is(":checked");
        var account = $(this)[0].offsetParent.id;
        if ($(this).is(":checked") === true) {
            // $('#check_a').append(account);

            $.ajax({
               url: '/cov_set/' + $('#cov_id').html(),
               type: 'post',
               data: {
                   check: $(this).val()
               },
                success: function (response) {
                    window.location.reload()
                }
            })

        } else {
            $('#check_a').filter(":contains(" + account + ")").remove()
        }
    }
)

// 'input[type="checkbox"]'




