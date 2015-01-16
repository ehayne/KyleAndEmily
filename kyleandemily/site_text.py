
from datetime import datetime
from pytz import timezone

WEDDING_DATE = datetime(2015, 04, 10, 14, 0, tzinfo=timezone('US/Central'))
ENGAGEMENT_DATE = 'Sunday, May 11, 2014'


ABOUT_TEXT = {
    'about_groom': 'Kyle grew up in Wisconsin until he was 19 years of age.  He then moved to San Francisco, California to ' +
                   'attend the Academy of Art University where he studied 3D character animation.  After graduation he ' +
                   'landed a job in Austin, TX at a studio that developed Playstation 3 games.',
    'about_bride': 'Emily was born in Canada but is a Texan at heart.  She grew up in Dallas and moved to Austin to attend the ' +
                   'University of Texas.  After a short time as a high school algebra teacher in Austin, she returned to the' +
                   'University as a software developer.',
    'engagement_story': 'It was a warm late spring Texas day with a slight breeze.  Kyle and Emily decide to spend the afternoon at the '+
                        'Driftwood Winery where they are members.  Kyle packed a picnic bag with the usuals but unknown to Emily there '+
                        'was also a hidden treasure. After talking most of the afternoon away, Kyle began to tell Emily about how amazing '+
                        'the last 2 years of his life has been with her.  He then got down on one knee and asked if she would like to marry him. '+
                        'She said YES!',
    'how_we_met': 'With 3 days left on Kyle''s match.com account, and only 3 days into the start of Emily''s match.com account ' +
                  '(Emily always was the lucky one), little did they know, this would be the start of an amazing adventure.  ' +
                  'After a few messages back and forth, Kyle cut to the chase and asked Emily to meet up at the local coffee shop.  ' +
                  'It was a beautiful spring afternoon in downtown Austin.  They talked for hours before realizing they hadn''t ordered ' +
                  'their coffee or tea yet.  The rest, as they say, is history!'
}

DETAILS_TEXT = {
    'ceremony': 'Our ceremony will be outdoors at the Winfield Inn. Please check back soon for the exact time we''re getting hitched!',
    'reception': 'Reception will follow at the Winfield Inn.',
    'dress_code': 'Dressy Casual',
    'driving_directions_text': 'We invite you to join us at the Winfield Inn in Kyle, Texas. It''s about 20 miles south of downtown Austin. ' +
                            'Expect some traffic on the way to the venue since it will be Friday evening.',
    'map_url': 'https://www.google.com/maps/embed/v1/place?q=The%20Winfield%20Inn%2C%20Scott%20Street%2C%20Kyle%2C%20TX%2C%20United%20States&key=AIzaSyD51KGRYE17Jnmouarr0-VubPV8Q_KXUpY'
}

HOTEL_TEXT = {
    'accomodations_text': '<p>We will be sharing our wedding weekend with many exciting events in Austin.' +
                          'Unfortunately, this means that we are unable to reserve a block at any of the hotels in town.' +
                          '</p>' +
                          '<p>' +
                          'We suggest taking advantage of the usual travel sites (expedia.com, hotels.com, etc) as well' +
                          'as trying out <a href="https://www.airbnb.com/">airbnb</a> and <a href="http://www.homeaway.com/">HomeAway</a>.' +
                          '</p>',
    'hotel_list': '',
    'activity_list': ''
}