
/*
    1. Splits the string using white spaces
    2. Map and process every word
    3. Join every word in a quote seperated by white spaces  
 */

const quote = "How can mirrors be real if our eyes aren't real";

function ToJaydenCase(str) { 
  return str.split(' ').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ')
  
 }

 console.log(ToJaydenCase(quote))
 