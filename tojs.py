import simplejson as json

rest = open('muconsole.html').read()
header, rest = rest.split('<!--SNIP1-->', 1)
_, rest = rest.split('/*---SNIP2---*/', 1)
css, rest = rest.split('/*---SNIP3---*/', 1)
_, rest = rest.split('<!--SNIP4-->', 1)
html, rest = rest.split('<!--SNIP5-->')
_, rest = rest.split('/*---SNIP6---*/')
js, rest = rest.split('/*---SNIP7---*/')

data = {
    'css': css,
    'html': html,
    'js': js,
}

js = u"""/* %s */
    var muconsoledata = %s;
    FB = window.FB;
    
    function create(tag, type, content, sid){
        var a = document.createElement(tag);
        if (type) {
            a.type=type;
        }
        if (sid) {
            a.id = sid;
        }
        a.innerHTML = content;
        document.body.appendChild(a);
    }
    
    if (!FB.MUConsole) {
        create('style', 'text/css', muconsoledata['css']);
        create('div', undefined, muconsoledata['html'], 'mubookmarklet');
        create('script', 'text/javascript', muconsoledata['js']);
    }
    
    FB.Event.subscribe('auth.statusChange', FB.MUConsole.gotStatus);
    FB.getLoginStatus();
    //FB.MUConsole.show();
""" % (header, json.dumps(data),)

open('muconsole.js', 'w').write(js)