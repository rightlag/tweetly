var errors = document.getElementById('errors');
errors.style.display = 'none';
var search = document.getElementById('search');
search.addEventListener('submit', getStatuses);
function getStatuses(event) {
  event.preventDefault();
  errors.style.display = 'none';
  if (errors.hasChildNodes()) {
    errors.removeChild(errors.childNodes[0]);
  }
  var input = {
    count: 1,
    screen_name: search.elements[0].value,
    include_rts: false,
    exclude_replies: true,
    contributor_details: true
  };
  search.reset();
  var settings = {
    contentType: 'application/json',
    data: JSON.stringify(input),
    type: 'POST'
  };
  var jqxhr = $.ajax('/fetch', settings);
  jqxhr.done(done);
  jqxhr.fail(fail);
  function done(tweets) {
    var tweet = tweets[0];
    var profileImageURL = document.getElementById('profile_image_url');
    profileImageURL.style.background = (
      "url('" + tweet.user.profile_image_url + "')" +
        " no-repeat center center"
    );
    profileImageURL.style.backgroundSize = 'cover';
    document.getElementById('name').innerHTML = tweet.user.name;
    document.getElementById('text').innerHTML = tweet.text;
    var urls = tweet.entities.urls;
    if (urls.length >= 1) {
      document.getElementById('url').href = urls[0].url;
    }
  }
  function fail(jqXHR) {
    var errorsArray = [];
    var i;
    if (jqXHR.responseJSON.hasOwnProperty('errors')) {
      // This represents an array of error messages.
      for (i = 0; i < jqXHR.responseJSON.errors.length; i++) {
        errorsArray.push(jqXHR.responseJSON.errors[i].message);
      }
    } else if (jqXHR.responseJSON.hasOwnProperty('error')) {
      // This represents a singleton error message.
      errorsArray.push(jqXHR.responseJSON.error);
    }
    for (i = 0; i < errorsArray.length; i++) {
      var node = document.createElement('li');
      node.className = 'mdl-list__item';
      var spanNode = document.createElement('span');
      spanNode.className = 'mdl-list__item-primary-content';
      var iconNode = document.createElement('i');
      iconNode.className = 'material-icons mdl-list__item-icon';
      iconNode.innerHTML = 'error';
      var textNode = document.createTextNode(errorsArray[i]);
      spanNode.appendChild(iconNode);
      spanNode.appendChild(textNode);
      node.appendChild(spanNode);
      errors.appendChild(node);
    }
    errors.style.display = 'block';
  }
}
