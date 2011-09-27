// CountDown v0.5 - A simple count down widget.
// Copyright (c) 2011 Nick Downing - ndowning@gmail.com
// Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
(function($, document, window) {

    // Milliseconds in a year, month, day, etc.
    var MS_PER = {
        year: 3.1556926e10,
        month: 2.62974383e9,
        day: 86400000,
        hour: 3600000,
        minute: 60000,
        second: 1000
    };

    // Abbreviations for the different countdown time components.
    var ABBREVIATIONS = {
        year: {
            symbol: '%y',
            label: 'yr'
        },
        month: {
            symbol: '%m',
            label: 'mth'
        },
        day: {
            symbol: '%d',
            label: 'day'
        },
        hour: {
            symbol: '%H',
            label: 'hr'
        },
        minute: {
            symbol: '%M',
            label: 'min'
        },
        second: {
            symbol: '%S',
            label: 'sec'
        }
    };

    // The components of the time delta in order of largest time unit to smallest
    // time unit.
    var COMPONENTS = ['year', 'month', 'day', 'hour', 'minute', 'second'];

    var CountDown = {
        init: function(options, elem) {
            this.options = $.extend({}, this.options, options);

            this.elem = elem;
            this.$elem = $(elem);

            this._timer = null;
            // This proxy is passed as the callback to setTimeout.
            this._tick_proxy = $.proxy(this, '_tick');

            this.start();
        },

        options: {
            // The reference time for the count down.  If ref_time is in the
            // past, then countdown will actually count up and provide an
            // elapsed time since ref_time.
            ref_time: (new Date()),

            // The interval between ticks of the countdown in milliseconds.
            // Defaults to 1 second.
            tick_interval: 1000,

            // Format for the countdown time output.  This is incredibily simple
            // for now.  You can use abbreviations for time period, and the
            // abbreviations will be replaced with the countdown time for that
            // period:
            //    %y - year, %m - month, %d - day, %H - hour, %M - minute,
            //    %S - second
            format: '%H:%M:%S',

            // Flag to indicate whether or not the countdown timer should display
            // a time if ref_time is in the past.
            allow_countup: false,

            // A callback invoked on each tick of the count down clock.
            // In the callback, this is the countdown widget.  The callback is
            // passed the time delta object containing year, month, day, hour,
            // minute, and second.
            //
            // If the callback handles the output of the count down, then return
            // false to have the widget skip the output.
            onTick: $.noop,

            // A callback that is invoked with the countdown reaches zero.
            // In the callback, this is the countdown widget.  Note:  If your
            // ref_time is in the past, then this event will never fire.
            onDone: $.noop
        },

        start: function() {
            if (this._timer) {
                return; // Count down is already running.
            }

            this._tick();
        },

        //
        // Returns the time delta since/until the ref_time.  The time delta returned
        // contains year, month, day, hour, minute, and second break down.
        //
        get_times: function() {
            return this._compute_time();
        },

        _schedule_tick: function() {
            this._timer = setTimeout(this._tick_proxy,
                                     this.options.tick_interval);
        },

        _tick: function() {
            var time = null;
            if (!$.contains(document, this.elem)) {
                return; // Element has been removed from the document.
            }

            time = this._compute_time();
            if (time === null) {
                this.options.onDone.call(this, time);
            } else {
                // If the callback returns false, then skip output and assume that
                // the callback handled it.
                if (this.options.onTick.call(this, time) !== false) {
                    this._update_display(time);
                }

                this._schedule_tick();
            }
        },

        _compute_time: function() {
            var now = new Date(),
                ref_time = this.options.ref_time,
                delta = ref_time - now,
                years = 0, months = 0, days = 0, hours = 0, minutes = 0, seconds = 0,
                time = {},
                i = 0,
                comp_name,
                ms_per;

            if (delta <= 0 && !this.options.allow_countup) {
                return null;
            } else {
                delta = Math.abs(delta);
            }

            for (i = 0; i < COMPONENTS.length; i++) {
                comp_name = COMPONENTS[i];
                ms_per = MS_PER[comp_name];
                if (delta >= ms_per) {
                    time[comp_name] = delta / ms_per;
                    delta = delta % ms_per;
                } else {
                    time[comp_name] = 0;
                }
            }

            // Whatever is left over is just milliseconds
            time.millisecond = delta;

            return time;
        },

        _update_display: function(time) {
            var time_str = null, i = 0, comp_name, abbrev, value;

            if (typeof this.options.format === 'function') {
                time_str = this.options.format(time, this);
            } else {
                time_str = new String(this.options.format);
                for (var i = 0; i < COMPONENTS.length; i++) {
                    comp_name = COMPONENTS[i];
                    time_comp = Math.floor(time[comp_name]);
                    abbrev = ABBREVIATIONS[comp_name];
                    value = time_comp < 10 ? "0"+time_comp : time_comp;
                    time_str = time_str.replace(abbrev.symbol, value);
                }
            }

            this.$elem.html(time_str);
        },

        _elem_in_document: function(elem) {
            return contains(document, elem);
        }
    };

    var obj_create = Object.create;
    if (typeof obj_create !== 'function') {
       obj_create = function(o) {
            function F() {}
            F.prototype = o;
            return new F();
        };
    }

    $.fn.countdown = function(options) {
        if (this.length) {
            return this.each(function() {
                var cd = obj_create(CountDown);
                cd.init(options, this);
                $.data(this, 'countdown', cd);
            });
        }
        return this;
    };

})(jQuery, document, this);