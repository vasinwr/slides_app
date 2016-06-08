console.log('asdf');
Mousetrap.bind(['right','space'], function() { alert('next page') });
Mousetrap.bind('left', function() { alert('previous page') });

var app = angular.module('lecture',[]);

app.factory('SharedData', function(){
  return { mainmenuHide: false };
});

app.controller('MenuController', function(SharedData){
  this.SharedData = SharedData;
  this.hover = false; 
  this.clicked = false;
  this.summ_hover  =false ;
  this.ques_hover  =false ;
  this.navi_hover  =false ;
  this.home_hover  =false ;
  this.close_hover =false ;
  this.ques = [{question: 'what happens if I fail?', votes: 10}, 
               {question: 'are labs open on bank holiday', votes: 8},
               {question: 'what happened to our coke machine', votes: 3}]
});




app.controller('SidesController', function(){
  this.left_hover = false; 
  this.right_hover = false;
});

app.controller('MainmenuController', function(SharedData){
  this.SharedData = SharedData;
  this.hide = false; 
  this.xs = [1,2,3,4,5];
  this.icon_hover = false;
});






app.directive('menuList', function(){
  return{
    restrict: 'E',
    templateUrl: 'ng_template/menu-list.html'
  };
});
