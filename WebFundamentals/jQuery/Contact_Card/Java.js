$(document).ready(function(){

    // $("#add_button").click(function(){
    //     $("#card1").append($("#first_name").val());
    //     $("#card1").append(" ");
    //     $("#card1").append($("#last_name").val());
    //     $(".description").css("display", "block");
    // });

    $("#add_button").click(function(){
        $("#right_wrapper").after("<div class="name_card"><p>");
        $("#right_wrapper").after($("#first_name").val());
        $("#right_wrapper").after(" ");
        $("#right_wrapper").after($("#last_name").val());
        $("#right_wrapper").after("</p><p class="description">Click for Description!</p>");
    });

    // $(document).on('click',"text", function(){
    //     $(".name_card").text($("des_box").val());
    // });
});
