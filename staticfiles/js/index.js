$(document).ready(function() {
    $("#msgs").on('change', function() {
        var num = this.value;
        if (num > 6) {
            alert("Can only accomodate 6 subjects at the moment!")
        } else {
            console.log(num);
            if (Math.floor(num) == num && $.isNumeric(num)) {
                $("#data-table").text('');

                for (var i = 1; i <= num; i++) {
                    $("#data-table").append("<label>I need</label>\
									<input placeholder='Z number of' type='text' name='subhour" + i + "'>\
									<label> hours to study</label>\
									<input placeholder='Subject " + i + "' type='text' name='sub" + i + "'>.<br><br>");
                }
                $("#submit-btn").html("<button type='submit' class='btn btn-lg btn-warning'>Calculate</button>");
            }
        };
    });

    $("#msgs").on('keydown', function(event) {
        if (event.keyCode == 13) {
            event.preventDefault();
            return false;
        }
    });
});