

var questions = [{
    imgSrc: "img/picture1.png" ,
    choices: ["Namibia", "DR Congo", "Mozambique", "Tanzania"],
    correctAnswer: 0
}, {
    imgSrc: "img/picture2.png" ,
    choices: ["Indonesia", "Poland", "Monaco", "Singapore"],
    correctAnswer: 2
}, {
    imgSrc: "img/picture3.png" ,
    choices: ["Ethiopia", "Ghana", "Myanmar", "Bolivia"],
    correctAnswer: 2
}, {
    imgSrc: "img/picture4.png" ,
    choices: ["Honduras", "El Salvador", "Nicaragua", "Lesotho"],
    correctAnswer: 1
}, {
    imgSrc: "img/picture5.png" ,
    choices: ["Oman", "Kuwait", "Sudan", "Jordan"],
    correctAnswer: 3
}];

var finish = false;
var currentQuestion = 0;
var correctAnswers = 0;
var selectedAnswer = [];

var c = 90;
var t;
$(document).ready(function ()
{
//####################################### START QUIZ BTN ######################################

  $("#startBtn").on("click" , function(){
      $("#startQuiz").css('display','none');

      displayCurrentQuestion();
      $("#quiz").css('display','block');
      $("#timerContainer").css('display','block');

      $("#quizMessage").hide();
      $("#backButton").attr('disabled', 'disabled');

      timer();
  })

  //#################################### DISPLAY CURRENT QUESTION ###############################

  function displayCurrentQuestion(){
    // Quiz is over
  	  if(c == 100) {
        c = 90;
        timer();}

      var q = questions[currentQuestion];
      var numChoices = q.choices.length;
      var choiceList = $("#choiceList");
      $(choiceList).find("li").remove();
      $("#image").attr("src",q.imgSrc);

      var choice;
      for (i = 0; i < numChoices; i++){

        choice = q.choices[i];
  		  if(selectedAnswer[currentQuestion] == i) {
  			     $('<li><input type="radio" class="radio-inline" checked="checked"  value=' + i + ' name="dynradio" />' +  ' ' + choice  + '</li>').appendTo(choiceList);
  		  } else {
  			     $('<li><input type="radio" class="radio-inline" value=' + i + ' name="dynradio" />' +  ' ' + choice  + '</li>').appendTo(choiceList);
  		    }
        }
      }

  //########################################### NEXT BUTTON CLICKED #################################

   $("#nextButton").on("click", function (){
       if (!finish) {
          var select = $("input[type='radio']:checked").val();
          if (select == undefined){
               $("#quizMessage").text("Please select an answer");
               $("#quizMessage").show();
           }
     else{

        $(document).find("#quizMessage").hide();
       if (select == questions[currentQuestion].correctAnswer)
         correctAnswers ++;

       selectedAnswer[currentQuestion] = select;

       currentQuestion ++;
       if(currentQuestion >= 1)
           $('#backButton').prop("disabled", false);

       if (currentQuestion < questions.length){
         displayCurrentQuestion();
      }
       else{
         $('#iTimeShow').html('Quiz Finished!');
         $('#timer').html("Your result: " + correctAnswers + " out of " + questions.length);
         $("#nextButton").css("display" , "none");
         $("#backButton").css("display" , "none");
         $("#playAgainButton").css('display','inline');
         c = 100;
         finish = true;
       }
     }
   }
});

   //########################################### BACK BUTTON CLICKED #################################

	$("#backButton").on("click", function (){
      if (!finish){
			   if(currentQuestion == 0) { return false; }

			   if(currentQuestion == 1) {
			         $("#backButton").attr('disabled', 'disabled');
			}
  			currentQuestion --;
				if (currentQuestion < questions.length){
					displayCurrentQuestion();
          var select = $("input[type='radio']:checked").val();
          if (select == questions[currentQuestion].correctAnswer)
            correctAnswers --;
      }
    }
  });

   //########################################### Play Again BUTTON CLICKED #################################

  $("#playAgainButton").on("click" , function(){

    currentQuestion = 0;
    selectedAnswer = [];
    correctAnswers = 0;
    finish = false
    c = 90;
    $('#iTimeShow').html('<i class="fa fa-stopwatch"></i>  Time Remaining');
    $('#timer').html("");
    timer();
    $("#playAgainButton").css('display','none');
    $("#nextButton").css("display" , "inline");
    $("#backButton").css("display" , "inline");
    displayCurrentQuestion();
  });
});
//########################################### TIMER FUNCTION #################################

function timer()
	{
		if(c == 100)
			return false;

		var minutes = parseInt( c / 60 ) % 60;
		var seconds = c % 60;
		var result =  (minutes < 10 ? "0" + minutes : minutes) + ":" + (seconds  < 10 ? "0" + seconds : seconds);
		$('#timer').html(result);

		if(c == 0 ){

        $('#iTimeShow').html('Quiz Finished!');
        $('#timer').html("Your result: " + correctAnswers + " out of " + questions.length);
        $('#iTimeShow').html('Quiz Finished!');
        $("#nextButton").css("display" , "none");
        $("#backButton").css("display" , "none");
        $("#playAgainButton").css('display','inline');
        c = 100;
        finish = true;
				return false;
		}

		c = c - 1;
		t = setTimeout(function()	{
			timer()
		},1000);
	}

function resetQuiz()
{

}
