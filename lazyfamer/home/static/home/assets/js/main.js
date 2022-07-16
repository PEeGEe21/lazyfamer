

(function($) {

	"use strict";

	// jQuery(document).ready(function($) {
      $('.sponsor').owlCarousel({
        items: 4,
        nav:false,
        //animateOut: 'fadeOut',
		// navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
		smartSpeed: 800,
        loop: true,
        margin: 10,
        autoplay: true,
        autoplaySpeed: 2000,
        navSpeed: 1000,
        paginationSpeed: 1000,
        slideSpeed: 1000,
        dots: false,
        responsive:{
            0:{
                items:3
            },
            650:{
                items:4
            },			
            1024:{
                items:4
            },
            1200:{
                items:5
            }
        }
      });

      $('.testimonial').owlCarousel({
        items: 4,
        nav:false,
        //animateOut: 'fadeOut',
		
		navText: ['<i class="fa fa-long-arrow-alt-left"></i>', '<i class="fa fa-long-arrow-alt-right"></i>'],
		smartSpeed: 800,
        loop: true,
        margin: 10,
        autoplay: true,
        autoplaySpeed: 2000,
        navSpeed: 1000,
        paginationSpeed: 1000,
        slideSpeed: 1000,
        dots: false,
        mouseDrag: false,
        touchDrag: false,
        pullDrag: false,
        responsive:{
            0:{
                items:1
            },
            650:{
                items:1
            },			
            1024:{
                items:2
            },
            1200:{
                items:2
            }
        }
      });

      $('.blog-slider').owlCarousel({
        items: 4,
        nav:false,
        //animateOut: 'fadeOut',
		
		navText: ['<i class="fa fa-long-arrow-alt-left"></i>', '<i class="fa fa-long-arrow-alt-right"></i>'],
		smartSpeed: 800,
        loop: true,
        // margin: 10,
        autoplay: true,
        autoplaySpeed: 2000,
        navSpeed: 1000,
        paginationSpeed: 1000,
        slideSpeed: 1000,
        dots: false,
        mouseDrag: false,
        touchDrag: false,
        pullDrag: false,
        responsive:{
            0:{
                items:1
            },
            650:{
                items:2
            },			
            1024:{
                items:3
            },
            1200:{
                items:3
            }
        }
      });
    // });

      var mobileBtn = $('.mobile_menu_btn');
      var mobileMenuWrapper = $('.mobile_menu_wrapper');

      mobileBtn.on('click', function(){
        mobileMenuWrapper.toggleClass('active')
      })

      var closeBtn = $('.closeBtn');

      closeBtn.on('click', function(){
        mobileMenuWrapper.removeClass('active');
          
      })


	


})(jQuery);
