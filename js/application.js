var BlogDirectory = {

    /*
     * Side Nav Affixing
     *
     * reference to:
     * https://github.com/twbs/bootstrap/blob/master/docs/assets/js/src/application.js#L35
     */
    setSideNavAffixing: function() {

        // Scrollspy
        var $window = $(window)
        var $body = $(document.body)

        $body.scrollspy({
            target: '.bs-docs-sidebar'
        })
        $window.on('load', function() {
            $body.scrollspy('refresh')
        })

        // Kill links
        $('.bs-docs-container [href=#]').click(function(e) {
            e.preventDefault()
        })

        // Sidenav affixing
        setTimeout(function() {
            var $sideBar = $('.bs-docs-sidebar')

            $sideBar.affix({
                offset: {
                    top: function() {
                        var offsetTop = $sideBar.offset().top
                        var sideBarMargin = parseInt($sideBar.children(0).css('margin-top'), 100)
                        var navOuterHeight = $('.bs-docs-bar-top').height()

                        return (this.top = offsetTop - navOuterHeight - sideBarMargin)
                    },
                    bottom: function() {
                        return (this.bottom = 0 - $('.bs-docs-container').outerHeight(true))
                    }
                }
            })
        }, 100)

        setTimeout(function() {
            $('.bs-top').affix()
        }, 100)
    }, // end of setSideNavAffixing:function()


    /* Generate directory tree
     *
     * side_nav_element: side navigation element
     * article_body_element:  article body container.
     *
     * processing: search header elements(h1,h2,h3) in `article_body_element`,
     * generate directory tree list, and put them into side_nav_element.
     */
    createBlogDirectory: function(side_nav_element, article_body_element) {
            if (!article_body_element || article_body_element.length < 1 ||
                !side_nav_element) {
                return false;
            }

            var nodes = article_body_element.find("h1,h2");
            var ulSideNav = side_nav_element;
            var lastlevel = 0;
            var level = 0;
            var html = "";
            $.each(nodes, function() {
                    lastlevel = level;
                    var $this = $(this);

                    var nodetext = $this.text();
                    // There maybe HTML tags in header inner text, use regex to erase them
                    nodetext = nodetext.replace(/<\/?[^>]+>/g, "");
                    nodetext = nodetext.replace(/&nbsp;/ig, "");

                    // btw: Jekyll generates id for each header.
                    var nodeid = $this.attr("id");
                    if (!nodeid) {
                        nodeid = "top";
                    }

                    var item_a = "<a href=\"#" + nodeid + "\">" + nodetext + "</a>";
                    /*$("<a></a>");
                    item_a.attr("href", "#" + nodeid);
                    item_a.text(nodetext);*/

                    var ret_li;
                    switch ($this.get(0).tagName) {
                        case "H1":
                            level = 1;
                            if (lastlevel == 0) {
                                ret_li = "<li>";
                            } else if (lastlevel == 1) {
                                ret_li = "</li><li>"
                            } else if (lastlevel == 2) {
                                ret_li = "</li></li></ul><li>"
                            }
                            break;
                        case "H2":
                            level = 2;
                            if (lastlevel == 0) {
                                ret_li = "<li><ul class=\"nav\"><li>";
                            } else if (lastlevel == 1) {
                                ret_li = "<ul class=\"nav\"><li>"
                            } else if (lastlevel == 2) {
                                ret_li = "</li><li>"
                            }
                            break;
                    }
                    ret_li += item_a;
                    if (!ret_li) {
                        // do nothing
                    } else {
                        html += ret_li;
                    }
                }) // end of each
            if (lastlevel == 1) {
                html += "</li>"
            } else if (lastlevel == 2) {
                html += "</li></li></ul>"
            }
            //console.log(html);
            html += "</br><a href=\"#top\">Back to top</a>"
            ulSideNav.append(html);
        } //end of createBlogDirectory:function()

};


jQuery(function($) {
    $(document).ready(function() {
        /* qrcode
        var opt = { text : window.location.href, width:150, height:150 };
        try {
            document.createElement("canvas").getContext("2d");
        } catch (e) {
            $.extend(opt,{ render : "table" });
        }
        $('.qrcode').html('').qrcode(opt);
    */

        // Generate the side navigation `ul` elements
        BlogDirectory.createBlogDirectory($("#sideNav"), $(".bs-docs-container"));

        // caculate affixing
        BlogDirectory.setSideNavAffixing();
    });
});