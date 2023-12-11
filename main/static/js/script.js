
document.getElementById("maindefault").click();
document.getElementById("jobdefault").click();
function mainTab(evt, tabName) {
    // Declare all variables
    var i, maintabcontent, maintablinks;
    
    // Get all elements with class="maintabcontent" and hide them
    maintabcontent = document.getElementsByClassName("maintabcontent");
    for (i = 0; i < maintabcontent.length; i++) {
      maintabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    maintablinks = document.getElementsByClassName("maintablinks");
    for (i = 0; i < maintablinks.length; i++) {
      maintablinks[i].className = maintablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";

  }
function providerTab(evt, tabName) {
    // Declare all variables
    var i, providercont, providertablinks;
    
    // Get all elements with class="maintabcontent" and hide them
    providercont = document.getElementsByClassName("providercont");
    for (i = 0; i < providercont.length; i++) {
      providercont[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    providertablinks = document.getElementsByClassName("providertablinks");
    for (i = 0; i < providertablinks.length; i++) {
      providertablinks[i].className = providertablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";

  }

  function jobTab(evt, jobNames) {
    // Declare all variables
    var i, jobtabcontent, jobtablinks;
    
    // Get all elements with class="jobtabcontent" and hide them
    jobtabcontent = document.getElementsByClassName("jobtabcontent");
    for (i = 0; i < jobtabcontent.length; i++) {
      jobtabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    jobtablinks = document.getElementsByClassName("jobtablinks");
    for (i = 0; i < jobtablinks.length; i++) {
      jobtablinks[i].className = jobtablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(jobNames).style.display = "block";
    evt.currentTarget.className += " active";

  }