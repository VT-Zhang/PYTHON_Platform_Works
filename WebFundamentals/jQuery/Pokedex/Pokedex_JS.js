$(document).ready(function(){
    //function to get the 151 photos appear on the left
    for (var i = 1; i < 152; i++){
        $("#main").append('<div id="' + i + '" class="pokes"><img src="http://pokeapi.co/media/img/' + i + '.png"></div>');
    }
    //function for click pokemon photo to show the information on the right
    $(document).on("click", ".pokes", function(){
        var num = $(this).attr("id");
        $.get('http://pokeapi.co/api/v1/pokemon/'+num+'/', function(res){
            var content = '<div class="name"><h2>' + res.name +'</h2></div>';
            content += '<div><img src="http://pokeapi.co/media/img/' + num + '.png"></div>';
            content += '<div><h3>Types</h4><br><ul  class="types">'
            for (let j = 0; j < res.types.length; j++){
                content += '<li>' + res.types[j].name + '</li>';
            }
            content += '</ul></div><br>';
            content += '<div><h3>Height</h3><p>' + res.height + '</p></div>';
            content += '<div><h3>Weight</h3><p>' + res.weight + '</p></div>';
            $("#info").html(content);
        },"json");
    });
});
