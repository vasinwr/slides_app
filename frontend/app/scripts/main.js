console.log('asdf');
Mousetrap.bind(['right','space'], function() { alert("next page") });
Mousetrap.bind('left', function() { alert("previous page") });

var app = angular.module('lecture',[]);
app.controller('MenuController', function(){
  this.hover = false; 
  this.menu_clicked = false;
});

app.directive('menuList', function(){
  return{
    restrict: 'E',
    templateUrl: 'ng_template/menu-list.html',
    link: function(scope, element){
      element.addClass('MyClass');
    }
  };
})
