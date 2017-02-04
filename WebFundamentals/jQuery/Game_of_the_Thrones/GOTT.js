$(document).ready(function() {

    $("#tar").click(function(){
        $.get('https://anapioficeandfire.com/api/houses/378', function(res){
            let content = '<div class="name"><p>Name: ' + res.name + '.</p>';
            content += '<p>Region: ' + res.region + '.</p>';
            content += '<p>Words: ' + res.words + '.</p>';
            content += '<p>Titles: ' + res.titles + '.</p>';
            content += '<p>Coat of Arms: ' + res.coatOfArms + '.</p>';
            content += '<p>Seats: ' + res.seats + '.</p>';
            content += '<p>Founded on: ' + res.founded + '.</p></div>';
            $("#details").html(content);
        },"json");
    });


    $("#stark").click(function(){
        $.get('https://anapioficeandfire.com/api/houses/362', function(res){
            let content = '<div class="name"><p>Name: ' + res.name + '.</p>';
            content += '<p>Region: ' + res.region + '.</p>';
            content += '<p>Words: ' + res.words + '.</p>';
            content += '<p>Titles: ' + res.titles + '.</p>';
            content += '<p>Coat of Arms: ' + res.coatOfArms + '.</p>';
            content += '<p>Seats: ' + res.seats + '.</p>';
            content += '<p>Founded on: ' + res.founded + '.</p></div>';
            $("#details").html(content);
        },"json");
    });


    $("#lannister").click(function(){
        $.get('https://anapioficeandfire.com/api/houses/229', function(res){
            let content = '<div class="name"><p>Name: ' + res.name + '.</p>';
            content += '<p>Region: ' + res.region + '.</p>';
            content += '<p>Words: ' + res.words + '.</p>';
            content += '<p>Titles: ' + res.titles + '.</p>';
            content += '<p>Coat of Arms: ' + res.coatOfArms + '.</p>';
            content += '<p>Seats: ' + res.seats + '.</p>';
            content += '<p>Founded on: ' + res.founded + '.</p></div>';
            $("#details").html(content);
        },"json");
    });

    $("#baratheon").click(function(){
        $.get('https://anapioficeandfire.com/api/houses/17', function(res){
            let content = '<div class="name"><p>Name: ' + res.name + '.</p>';
            content += '<p>Region: ' + res.region + '.</p>';
            content += '<p>Words: ' + res.words + '.</p>';
            content += '<p>Titles: ' + res.titles + '.</p>';
            content += '<p>Coat of Arms: ' + res.coatOfArms + '.</p>';
            content += '<p>Seats: ' + res.seats + '.</p>';
            content += '<p>Founded on: ' + res.founded + '.</p></div>';
            $("#details").html(content);
        },"json");
    });
});
