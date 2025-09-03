" plugin/roscompile.vim
let g:ale_cpp_clangd_executable = '/usr/bin/clangd-10'
let g:ale_cpp_clangtidy_executable = '/usr/bin/clang-tidy-10'



function! s:SetCompileCommandsFromScript() abort
	let l:script = expand('<sfile>:p:h:h') . 'python/ycm_like_behavior.py'
	let l:file = expand('%:p')
	"echom 'called ycm_like_behavior.py'
	let l:dir = system('python ' . shellescape(l:script) . ' ' . shellescape(l:file))
	let l:dir = substitute(l:dir, '\n+\$', '', '')

	if !empty(l:dir)
		"let b:ale_c_cc_options = '--compile-commands-dir=' . l:dir
		let g:ale_linters = {
					\ 'cpp': ['clangd', 'clangtidy'],
					\ }
		"let b:ale_cpp_clangtidy_options = '-p=' . l:dir
		let b:ale_c_build_dir = l:dir
		"let b:ale_c_clangd_options = '--compile-commands-dir=' . l:dir
		"let b:ale_cpp_clangd_options = '--compile-commands-dir=' . l:dir
	"else
	"	let b:ale_c_clangd_options = 'iofjasdifjaosidjfgaoisdjaoidfgjaorighjqeroh' . l:dir
	"	let b:ale_cpp_clangd_options = 'iofjasdifjaosidjfgaoisdjaoidfgjaorighjqeroh' . l:dir

	endif
endfunction

augroup ROSClangd
	autocmd!
	"echom 'got here'
	autocmd FileType cpp call s:SetCompileCommandsFromScript()
augroup END
