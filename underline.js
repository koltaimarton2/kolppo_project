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
