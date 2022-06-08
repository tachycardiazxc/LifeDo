(function() {
    $("#makeEditable").click(function() {
        $('input:text').removeAttr("readonly");
    });
    $("#makeNonEditable").click(function(e) {

                // If you submit the for without ajax
                // then just make the text field default readonly="readonly"

            // OR

                // If you submit the form using ajax then use
                // $('input:text').removeAttr("readonly");
                // within success function
    });
});