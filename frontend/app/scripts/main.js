console.log('asdf');
Mousetrap.bind(['right','space'], function() { alert('next page') });
Mousetrap.bind('left', function() { alert('previous page') });

var app = angular.module('lecture',[]);
app.controller('MenuController', function(){
  this.hover = false; 
  this.clicked = false;
  this.summ_hover  = false;
  this.ques_hover  = false;
  this.navi_hover  = false;
  this.home_hover  = false;
  this.close_hover = false;
});

app.directive('menuList', function(){
  return{
    restrict: 'E',
    templateUrl: 'ng_template/menu-list.html'
  };
});


app.controller('SidesController', function(){
  this.left_hover = false; 
  this.right_hover = false;
});
