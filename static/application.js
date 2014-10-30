/*
 * Application Initialization
 * 
 * Date Created 5/12/2012
 * Last Update 5/12/2012
 *
 * This theme is part of themeforest.net
 * ====================================================================================================================== */
// Mobile Menu
;(function ( $, window, document, undefined ) {
	
	'use strict';
	
    var pluginName = "mobileMenu",
        defaults = {
            target: "#nav-mainmenu"
        };

    function Plugin( element, options ) {
        this.element = element;
        this.options = $.extend( {}, defaults, options );
        this._defaults = defaults;
        this._name = pluginName;

        this.init();
    }

    Plugin.prototype = {

        init: function() {
			this.toggleLayout(this.element, this.options)
        },

        toggleLayout: function(el, opt) {
			$(el).click(function(e) {
				$(opt.target).toggleClass('show');
				$(this).toggleClass('open');
					
				e.preventDefault();
			});
        }
    };

    $.fn[pluginName] = function ( options ) {
        return this.each(function () {
            if (!$.data(this, "plugin_" + pluginName)) {
                $.data(this, "plugin_" + pluginName, new Plugin( this, options ));
            }
        });
    };

})( jQuery, window, document );$('[data-menu=mobile]').mobileMenu();


// Layout Switcher
;(function ( $, window, document, undefined ) {
	
	'use strict';
	
    var pluginName = "layoutSwitcher",
        defaults = {
            target: "#wrapper",
			layout: ""
        };

    function Plugin( element, options ) {
        this.element = element;
        this.options = $.extend( {}, defaults, options );
        this._defaults = defaults;
        this._name = pluginName;

        this.init();
    }

    Plugin.prototype = {

        init: function() {
			this.toggleLayout(this.element, this.options)
        },

        toggleLayout: function(el, opt) {
            $(el).live('click',function() {
				$(opt.target).removeAttr('class');
				$(opt.target).attr('class', opt.layout);
			});
        }
    };

    $.fn[pluginName] = function ( options ) {
        return this.each(function () {
            if (!$.data(this, "plugin_" + pluginName)) {
                $.data(this, "plugin_" + pluginName, new Plugin( this, options ));
            }
        });
    };

})( jQuery, window, document );$('[data-layout="boxed"]').layoutSwitcher({ layout: "boxed" });$('[data-layout="full"]').layoutSwitcher();


// Pattern Switcher
;(function ( $, window, document, undefined ) {
	
	'use strict';
	
    var pluginName = "patternSwitcher",
        defaults = {
            target: ""
        };

    function Plugin( element, options ) {
        this.element = element;
        this.options = $.extend( {}, defaults, options );
        this._defaults = defaults;
        this._name = pluginName;

        this.init();
    }

    Plugin.prototype = {

        init: function() {
			this.togglePattern(this.element, this.options)
        },

        togglePattern: function(el, opt) {
            $(el).live('click',function() {
				$(opt.target).removeAttr('class');
				$(opt.target).attr('class', $(this).attr('class'));
			});
        }
    };

    $.fn[pluginName] = function ( options ) {
        return this.each(function () {
            if (!$.data(this, "plugin_" + pluginName)) {
                $.data(this, "plugin_" + pluginName, new Plugin( this, options ));
            }
        });
    };

})( jQuery, window, document );$('[data-menu="bodypattern"]').patternSwitcher({ target : 'body' });$('[data-menu="wrapperpattern"]').patternSwitcher({ target : '#wrapper-inner' });

var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-37555954-1']);
_gaq.push(['_setDomainName', '5gbfree.com']);
_gaq.push(['_trackPageview']);

(function() {
var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();