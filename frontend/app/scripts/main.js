console.log('asdf');
Mousetrap.bind(['right','space'], function() { alert('next page') });
Mousetrap.bind('left', function() { alert('previous page') });

var app = angular.module('lecture',[]);
app.controller('MenuController', function(){
  this.hover = false; 
  this.clicked = false;
});

app.directive('menuList', function(){
  return{
    restrict: 'E',
    templateUrl: 'ng_template/menu-list.html'
  };
});

