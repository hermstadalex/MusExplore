#!/usr/bin/env python3



import pitchfork


def pfork_test( request ):

    p = pitchfork.search('kanye west', 'my beautiful')

    print( p.album() )

    print( p.score() )

    return render(request, {'score': p.score(), 'album': p.album() })
