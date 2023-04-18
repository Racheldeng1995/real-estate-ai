$(document).ready(function() {
    $('#search-form').on('submit', function(event) {
      event.preventDefault();
      var city = $('#city').val();
      var state = $('#state').val();
  
      $.ajax({
        url: '/search',
        data: {
          'city': city,
          'state': state
        },
        success: function(data) {
          $('#search-results').html(data);
        }
      });
    });
  });
  