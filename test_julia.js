import * as fs from 'fs'
import * as sedlex from './fable_sedlex/Sedlex.js'
import * as codegen_julia from './fable_sedlex/CodeGen.Julia.js'
import * as pretty_doc from './fable_sedlex/PrettyDoc.js'
import { pinterval, pchar, pseq, por, pplus, popt, pstar, pcompl, pchars, pstring, peof, pany } from './fable_sedlex/Sedlex.js'
import { Lexer_discard, Lexer_tokenize } from './fable_sedlex/Sedlex.js'

const digit = pinterval('0'.charCodeAt(0), '9'.charCodeAt(0))
const dquote = pchar('"')
const backslash = pchar('\\')
const dot = pchar('.')
const exp = pseq([por(pchar('E'), pchar('e')), pplus(digit)])
const flt = pseq([pstar(digit), dot, pplus(digit), popt(exp)])
const integral = pseq([pplus(digit), popt(exp)])
const string_lit = pseq([dquote, pstar(por(pcompl(dquote), pseq([backslash, pany]))), dquote])
const space = pchars(["\n", "\t", "\r", ' '])
const EOF_ID = 0

function main()
{


    let cu = sedlex.build(
        [
            [space, Lexer_discard],
            [flt, Lexer_tokenize(1)],
            [integral, Lexer_tokenize(2)],
            [string_lit, Lexer_tokenize(3)],
            [pstring("+"), Lexer_tokenize(4)],
            [pstring("+="), Lexer_tokenize(4)],
            [peof, Lexer_tokenize(EOF_ID)]
        ], "my error")


    let header = `
using Sedlex
is_eof(x) = x.token_id == 0
    `
    let code = codegen_julia.codegen_julia(header, cu)
    fs.writeFileSync("generated.jl", pretty_doc.showDoc(code), {encoding: 'utf8'})
}

main()
