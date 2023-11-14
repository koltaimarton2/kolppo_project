let menu = document.getElementsByClassName( 'nav' );
if ( menu ) {  
let menu_slider_hover = document.getElementById( 'nav_slide_hover' );
  if ( menu_slider_hover ) {
    nav_slider( menu[0], function( el, width, tempMarginLeft ) {                          
      el.onmouseover = () => {
        menu_slider_hover.style.width =  width + '%';                    
        menu_slider_hover.style.marginLeft = tempMarginLeft + '%';    
      }
    });
  }
} 

function nav_slider( menu, callback ) {
  let menu_width = menu.offsetWidth;
  menu = menu.getElementsByTagName( 'li' );            
  if ( menu.length > 0 ) {
    var marginLeft = [];
    [].forEach.call( menu, ( el, index ) => {
      var width = getPercentage( el.offsetWidth, menu_width );                              
      var tempMarginLeft = 0;
      if ( index != 0 )  {
        tempMarginLeft = getArraySum( marginLeft );
      }            
      callback( el, width, tempMarginLeft );     
      marginLeft.push( width );
    } );
  }
}

function getPercentage( min, max ) {
  return min / max * 100;
}

function getArraySum( arr ) {
  let sum = 0;
  [].forEach.call( arr, ( el, index ) => {
    sum += el;
  } );
  return sum;
}


var count = 0;
var oElement;

function changec(e) {
  e = e || window.event;
  var target = e.target || e.srcElement;
  var parent = target.parentNode.parentNode.parentNode;
  console.log(parent.parentNode);
  console.log(parent.children[0]);
  console.log(parent.children[0].children[1].children[0].children[0]);
  count++;
  console.log("COUNT:" + count);
        if(count%2==1) {
          parent.style.width = "100%";
          var h = parent.parentNode.clientHeight * 1 + "px";
          parent.parentNode.parentNode.style.height = h;
          parent.parentNode.style.height = h;
          parent.style.height = h;
          parent.children[0].children[1].children[0].children[0].style.maxHeight = h;
          parent.children[0].children[1].children[0].children[0].style.height = "100%";
          parent.style.zIndex = 1000;
          parent.style.display = "block";
          var elements = document.getElementsByClassName("col-xl-4");
          Array.prototype.forEach.call(elements, function(element) {
            if(element != parent) {
              element.style.display = "none";
              oElement = element;
            }
          });
          console.log("OELEMENT: " + oElement);
        }
        else {
          parent.style.width = oElement.style.width;
          console.log("OELEMENT: " + oElement);

          parent.children[0].children[1].children[0].children[0].style.maxHeight = oElement.children[0].children[1].children[0].children[0].style.maxHeight;
          parent.children[0].children[1].children[0].children[0].style.height = oElement.children[0].children[1].children[0].children[0].style.height;
          parent.style.height = oElement.style.height;

          parent.parentNode.parentNode.style.height = oElement.parentNode.parentNode.style.height;
          parent.parentNode.style.height = oElement.parentNode.style.height;


          parent.style.zIndex = 1000;
          parent.style.display = "block";
          var elements = document.getElementsByClassName("col-xl-4 ");
          Array.prototype.forEach.call(elements, function(element) {
            // Do stuff here
            if(element != parent) {
              console.log(element);
              element.style.display = "block";
            }
          });
        }
}