function my_decode(t) {
                        var e = (t = String(t).replace('a', "")).length;
                        e % 4 == 0 && (e = (t = t.replace(/==?$/, "")).length),
                        (e % 4 == 1 || /[^+a-zA-Z0-9/]/.test(t)) && l("Invalid character: the string to be decoded is not correctly encoded.");
                        for (var n, r, i = 0, o = "", a = -1; ++a < e; )
                            r = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".indexOf(t.charAt(a)),
                            n = i % 4 ? 64 * n + r : r,
                            i++ % 4 && (o += String.fromCharCode(255 & n >> (-2 * i & 6)));
                        return o
                    }