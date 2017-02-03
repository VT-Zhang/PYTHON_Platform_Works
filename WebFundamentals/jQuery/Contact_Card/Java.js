$(document).ready(function(){

    // $("#add_button").click(function(){
    //     $("#card1").append($("#first_name").val());
    //     $("#card1").append(" ");
    //     $("#card1").append($("#last_name").val());
    //     $(".description").css("display", "block");
    // });
    var counter = 1;

    $("#add_button").click(function(){
        var content = '<div class="name_card" id="' + counter + '"> <p>' + $("#first_name").val() + ' ' + $("#last_name").val() + '</p>';
        content += '<p class="description">Click for Description!</p></div>';
        $("#right_wrapper").html(content);
        counter++;
    });

    // $(document).on('click',"text", function(){
    //     $(".name_card").text($("des_box").val());
    // });
    $(document).on("click", ".name_card", function(){
        var num = $(this).attr("#id");
        $('#id' + num).html($("#des_box".val()));
    });

});
