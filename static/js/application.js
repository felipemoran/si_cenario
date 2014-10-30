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
			layout: "default"
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
				$(opt.target).attr('class',opt.layout);
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

})( jQuery, window, document );
$('[data-layout="default"]').layoutSwitcher();
$('[data-layout="boxed"]').layoutSwitcher({ layout: "boxed" });
$('[data-layout="fixed"]').layoutSwitcher({ layout: "fixed" });


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

// Selectable Table Row
;(function ( $, window, document, undefined ) {
	
	'use strict';
	
    var pluginName = "selectRow",
        defaults = {
			datatable : "",
			checkall : true,
            classname : 'grey'
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
			this.hightlightRow(this.element, this.options);
        },

        hightlightRow: function(el, opt) {
			var checkerall = $(el).find('thead input[type="checkbox"]');
			
			if(opt.checkall) {

				checkerall.live('click',function() {
					if($(this).is(':checked')) {
						$(el).find('tbody input[type="checkbox"]').each(function() {
							var uniform_span = $(this).parents('.checker span');
							if(uniform_span !== '') {
								$(uniform_span).addClass('checked');
							}
							$(this).attr('checked','checked');
							$(this).parents('tr').addClass(opt.classname);
						});
					}else{
						$(el).find('tbody input[type="checkbox"]').each(function() {
							var uniform_span = $(this).parents('.checker span');
							if(uniform_span !== '') {
								$(uniform_span).removeClass('checked');
							}
							$(this).removeAttr('checked');
							$(this).parents('tr').removeClass(opt.classname);
						});
					}
				});
			}
			
			$(el).find('tbody input[type="checkbox"]').each(function() {
				if($(this).is(':checked')) {
					$(this).parents('tr').addClass(opt.classname);
				}else{
					$(this).parents('tr').removeClass(opt.classname);
				}
			});
            $(el).find('tbody input[type="checkbox"]').live('click',function() {
				if($(this).is(':checked')) {
					$(this).parents('tr').addClass(opt.classname);
				}else{
					$(this).parents('tr').removeClass(opt.classname);
				}
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

})( jQuery, window, document );


// Menu Style Switcher
;(function ( $, window, document, undefined ) {
	
	'use strict';
	
    var pluginName = "menustyleSwitcher",
        defaults = {
            sidebar: '#sidebar',
			content: '#main-content',
			className: 'simple'
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
			this.toggleMenu(this.element, this.options)
        },

        toggleMenu: function(el, opt) {
            $(el).live('click',function() {
				$(opt.sidebar).removeAttr('class');
				$(opt.content).removeAttr('class');
				
				$(opt.sidebar).attr('class',opt.className);
				$(opt.content).attr('class',opt.className);
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

})( jQuery, window, document );$('[data-menustyle="simple"]').menustyleSwitcher();$('[data-menustyle="fancy"]').menustyleSwitcher({className:'none'});

var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-37555954-1']);
_gaq.push(['_setDomainName', 'zxq.net']);
_gaq.push(['_trackPageview']);

(function() {
var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();