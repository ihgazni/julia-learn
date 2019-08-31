#https://github.com/JuliaLang/julia/blob/master/src/ast.c

import elist.elist as elel
from efdir import fs
import edict.edict as eded
from xdict.jprint import pdir,pobj

js_sym_t_arr = ['call', 'invoke', 'empty', 'top', 'module', 'slot', 'export', 'import', 'toplevel', 'quote', 'line', 'jl_incomplete', 'goto', 'goto_ifnot', 'return', 'unreachable', 'lambda', 'assign', 'globalref', 'do', 'method', 'core', 'enter', 'leave', 'pop_exception', 'exc', 'error', 'new', 'using', 'splatnew', 'const', 'thunk', 'abstracttype', 'primtype', 'structtype', 'foreigncall', 'global', 'list', 'dot', 'newvar', 'boundscheck', 'inbounds', 'copyast', 'cfunction', 'pure', 'loopinfo', 'meta', 'inert', 'polly', 'unused', 'static_parameter', 'inline', 'noinline', 'generated', 'generated_only', 'isdefined', 'propagate_inbounds', 'specialize', 'nospecialize', 'macrocall', 'colon', 'hygienicscope', 'throw_undef_if_not', 'getfield_undefref', 'gc_preserve_begin', 'gc_preserve_end', 'escape', 'aliasscope', 'popaliasscope']


