let mapleader=" "
set nocompatible
set encoding=utf-8
syntax on
filetype on
filetype plugin on
filetype indent on
filetype plugin indent on
set number
" set norelativenumber
set relativenumber
" 下面的函数作用:normal模式下使用相对行号;insert模式下使用绝对行号
augroup relative_number
	autocmd!
	autocmd InsertEnter * :set norelativenumber
	autocmd InsertLeave * :set relativenumber
augroup END
set ruler
set cursorline
set autoindent
set cindent
set smartindent
set showmode
exec "nohlsearch"
set ignorecase
set smartcase
set tabstop=4
set wildmenu
" This specifies where in Insert mode the <BS> is allowed to delete the
" character in front of the cursor. The three items,separated by comma,tell
" Vim to delete the white space at the start of the line,a line break and the
" character before where Insert mode started.
set backspace=indent,eol,start
"Keep 50 commands and 50 search patterns in the history.Use another number if
"you want to remember fewer or more lines.
set history=50
"Display an incomplete command in the lower corner of the Vim window, left of
"the ruler.For example,when you type "2f",Vim is waiting for you to type the
"character to find and "2f" is displayed. When you press "w" next, the "2fw"
"command is executed and the displayed "2f" is removed.
set showcmd
" Display matches for a search pattern while you type.
set incsearch
" This switches on syntax highlighting. And the 'hlsearch' option tells Vim to
" highlight matches with the last used search pattern. The "if" command is
" very useful to set options only when some condition is met.
set hlsearch
" Disable 's' default key
map s <nop>
" Save and Quit
noremap S :w<CR>
noremap Q :q<CR>
" Using <leader>+arrows for moving cursor between windows
map <leader>h <C-w>h
map <leader>l <C-w>l
map <leader>i <C-w>k
map <leader>m <C-w>j
" Moving cursor in Insert mode
inoremap <C-f> <Left>
inoremap <C-b> <Right>
inoremap <C-k> <Up>
inoremap <C-l> <Down>
" Split screen to Up/Down(Horizontal),Left/Right(Vertical)
noremap si :set nosplitbelow<CR>:split<CR>:set splitbelow<CR>
noremap sm :set splitbelow<CR>:split<CR>
noremap sl :set nosplitright<CR>:vsplit<CR>:set splitright<CR>
noremap sj :set splitright<CR>:vsplit<CR>
" Resize splits by arrow keys
noremap <Up> :res +5<CR>
noremap <Down> :res -5<CR>
noremap <Left> :vertical resize -5<CR>
noremap <Right> :vertical resize +5<CR>
" Reload vimrc
noremap R :source ${MYVIMRC}<CR>

" 光标停留在上次退出的位置
" if has(“autocmd”)
"     au BufReadPost * if line(“’\”“) > 1 && line(“’\”“) <= line(“$”) | exe “normal! g’\”” | endif
" au BufReadPost * if line("'"") > 0|if line("'"") <= line("$")|exe("norm '"")|else|exe "norm $"|endif|endif
" endif

" Plugins installation - Using vim-plug
call plug#begin('~/.vim/plugged')
" Previewing of Markdown
Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app && yarn install'  }
" Syntax highlighting for Markdown
Plug 'godlygeek/tabular'
Plug 'plasticboy/vim-markdown'
" Creating table in Markdown
Plug 'dhruvasagar/vim-table-mode'
" Surrounding
Plug 'tpope/vim-surround'
" Insert or Delete brackets,parens,quotes in pair
Plug 'jiangmiao/auto-pairs'
" Ultisnips
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'
" NERDTree
Plug 'preservim/nerdtree'
Plug 'Xuyuanp/nerdtree-git-plugin'
" Themes
Plug 'altercation/vim-colors-solarized'
Plug 'tomasr/molokai'
Plug 'dracula/vim'
Plug 'NLKNguyen/papercolor-theme'
" Beautiful icons for files
Plug 'ryanoasis/vim-devicons'
" Status bar
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
" coc.nvim
Plug 'neoclide/coc.nvim', {'branch': 'release'}
" Copyright
Plug 'nine2/vim-Copyright'
" Nerdcommenter
Plug 'preservim/nerdcommenter'
" Powerline - status bar
Plug 'powerline/powerline'
" Watatime - coding log
Plug 'wakatime/vim-wakatime'
" tagbar
Plug 'majutsushi/tagbar'
" Bullets - a vim plugin for automated bullet lists
Plug 'dkarter/bullets.vim'
" Nerdtree-syntax
" Plug 'tiagofume/vim-nerdtree-syntax-highlight'
Plug 'vwxyutarooo/nerdtree-devicons-syntax'
" Calender
Plug 'itchyny/calendar.vim'
" Indent-guides
Plug 'nathanaelkane/vim-indent-guides'
" Signature - for bookmark
Plug 'kshenoy/vim-signature'
" Zeavim, Zeal for Vim
Plug 'KabbAmine/zeavim.vim'
" Debugger
" Plug 'puremourning/vimspector', { 'do': './install_gadget.py
" --enable-python --enable-go --enable-bash' }
"  Thesaurus
Plug 'beloglazov/vim-online-thesaurus'
Plug 'ron89/thesaurus_query.vim'
" Fuzzy finder
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
" Far.vim - find and replace vim plugin
Plug 'brooth/far.vim'
" emmet - for Html
Plug 'mattn/emmet-vim'
" webapi-vim
Plug 'mattn/webapi-vim'
" YouCompleteMe
" Plug 'ycm-core/YouCompleteMe'
call plug#end()

" markdown-preview.nvim
let g:mkdp_auto_start = 0
let g:mkdp_auto_close = 1
let g:mkdp_refresh_slow = 0
let g:mkdp_command_for_global = 0
let g:mkdp_open_to_the_world = 0
let g:mkdp_open_ip = ''
let g:mkdp_browser = ''
let g:mkdp_echo_preview_url = 0
let g:mdkp_browserfunc = ''
let g:mkdp_preview_options = {
    \ 'mkit': {},
    \ 'katex': {},
    \ 'uml': {},
    \ 'maid': {},
    \ 'disable_sync_scroll': 0,
    \ 'sync_scroll_type': 'middle',
    \ 'hide_yaml_meta': 1,
    \ 'sequence_diagrams': {},
    \ 'flowchart_diagrams': {},
    \ 'content_editable': v:false,
    \ 'disable_filename': 0
    \ }
let g:mkdp_markdown_css = ''
let g:mkdp_highlight_css = ''
let g:mkdp_port = ''
let g:mkdp_page_title = '「${name}」'

" vim-table-mode
map <leader>tm :TableModeToggle<CR>
function! s:isAtStartOfLine(mapping)
  let text_before_cursor = getline('.')[0 : col('.')-1]
  let mapping_pattern = '\V' . escape(a:mapping, '\')
  let comment_pattern = '\V' . escape(substitute(&l:commentstring, '%s.*$', '', ''), '\')
  return (text_before_cursor =~? '^' . ('\v(' . comment_pattern . '\v)?') . '\s*\v' . mapping_pattern . '\v$')
endfunction

inoreabbrev <expr> <bar><bar>
          \ <SID>isAtStartOfLine('\|\|') ?
          \ '<c-o>:TableModeEnable<cr><bar><space><bar><left><left>' : '<bar><bar>'
inoreabbrev <expr> __
          \ <SID>isAtStartOfLine('__') ?
          \ '<c-o>:silent! TableModeDisable<cr>' : '__'

" Ultisnips
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<c-b>"
let g:UltiSnipsJumpBackwardTrigger="<c-z>"

" Nerdtree
let NERDTreeShowLineNumbers=1
let NERDTreeAutoCenter=1
let NERDTreeShowHidden=1
let NERDTreeWinSize=21
let g:nerdtree_tabs_open_on_console_startup=1
let NERDTreeIgnore=['\.pyc','\~s','\.swp']
let NERDTreeShowBookmarks=1
map <F2> :NERDTreeMirror<CR>
map <F2> :NERDTreeToggle<CR>
autocmd VimEnter * NERDTree
wincmd w
autocmd VimEnter * wincmd w

" NERDTree-git-plugin
let g:NERDTreeGitStatusIndicatorMapCustom = {
    \ 'Modified'  :'✹',
    \ 'Staged'    :'✚',
    \ 'Untracked' :'✭',
    \ 'Renamed'   :'➜',
    \ 'Unmerged'  :'═',
    \ 'Deleted'   :'✖',
    \ 'Dirty'     :'✗',
    \ 'Ignored'   :'☒',
    \ 'Clean'     :'✔︎',
    \ 'Unknown'   :'?',
    \ }

" airline
let g:airline_section_b = '%{strftime("%c")}'
let g:airline_section_y = 'BN: %{bufnr("%")}'
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#left_sep = ' '
let g:airline#extensions#tabline#left_alt_sep = '|'
let g:airline_statusline_ontop = 0

" coc.vim
" TextEdit might fail if hidden is not set.
set hidden

" Some servers have issues with backup files, see #649.
set nobackup
set nowritebackup

" Give more space for displaying messages.
set cmdheight=2

" Having longer updatetime (default is 4000 ms = 4 s) leads to noticeable
" delays and poor user experience.
set updatetime=300

" Don't pass messages to |ins-completion-menu|.
set shortmess+=c

" Always show the signcolumn, otherwise it would shift the text each time
" diagnostics appear/become resolved.
if has("patch-8.1.1564")
  " Recently vim can merge signcolumn and number column into one
  set signcolumn=number
else
  set signcolumn=yes
endif

" Use tab for trigger completion with characters ahead and navigate.
" NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
" other plugin before putting this into your config.
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use <c-space> to trigger completion.
if has('nvim')
  inoremap <silent><expr> <c-space> coc#refresh()
else
  inoremap <silent><expr> <c-@> coc#refresh()
endif

" Make <CR> auto-select the first completion item and notify coc.nvim to
" format on enter, <cr> could be remapped by other vim plugin
inoremap <silent><expr> <cr> pumvisible() ? coc#_select_confirm()
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

" Use `[g` and `]g` to navigate diagnostics
" Use `:CocDiagnostics` to get all diagnostics of current buffer in location list.
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)

" GoTo code navigation.
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Use K to show documentation in preview window.
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  elseif (coc#rpc#ready())
    call CocActionAsync('doHover')
  else
    execute '!' . &keywordprg . " " . expand('<cword>')
  endif
endfunction

" Highlight the symbol and its references when holding the cursor.
autocmd CursorHold * silent call CocActionAsync('highlight')

" Symbol renaming.
nmap <leader>rn <Plug>(coc-rename)

" Formatting selected code.
xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

augroup mygroup
  autocmd!
  " Setup formatexpr specified filetype(s).
  autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
  " Update signature help on jump placeholder.
  autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
augroup end

" Applying codeAction to the selected region.
" Example: `<leader>aap` for current paragraph
xmap <leader>a  <Plug>(coc-codeaction-selected)
nmap <leader>a  <Plug>(coc-codeaction-selected)

" Remap keys for applying codeAction to the current buffer.
nmap <leader>ac  <Plug>(coc-codeaction)
" Apply AutoFix to problem on the current line.
nmap <leader>qf  <Plug>(coc-fix-current)

" Map function and class text objects
" NOTE: Requires 'textDocument.documentSymbol' support from the language server.
xmap if <Plug>(coc-funcobj-i)
omap if <Plug>(coc-funcobj-i)
xmap af <Plug>(coc-funcobj-a)
omap af <Plug>(coc-funcobj-a)
xmap ic <Plug>(coc-classobj-i)
omap ic <Plug>(coc-classobj-i)
xmap ac <Plug>(coc-classobj-a)
omap ac <Plug>(coc-classobj-a)

" Remap <C-f> and <C-b> for scroll float windows/popups.
" Note coc#float#scroll works on neovim >= 0.4.3 or vim >= 8.2.0750
nnoremap <nowait><expr> <C-f> coc#float#has_scroll() ? coc#float#scroll(1) : "\<C-f>"
nnoremap <nowait><expr> <C-b> coc#float#has_scroll() ? coc#float#scroll(0) : "\<C-b>"
inoremap <nowait><expr> <C-f> coc#float#has_scroll() ? "\<c-r>=coc#float#scroll(1)\<cr>" : "\<Right>"
inoremap <nowait><expr> <C-b> coc#float#has_scroll() ? "\<c-r>=coc#float#scroll(0)\<cr>" : "\<Left>"

" NeoVim-only mapping for visual mode scroll
" Useful on signatureHelp after jump placeholder of snippet expansion
if has('nvim')
  vnoremap <nowait><expr> <C-f> coc#float#has_scroll() ? coc#float#nvim_scroll(1, 1) : "\<C-f>"
  vnoremap <nowait><expr> <C-b> coc#float#has_scroll() ? coc#float#nvim_scroll(0, 1) : "\<C-b>"
endif

" Use CTRL-S for selections ranges.
" Requires 'textDocument/selectionRange' support of language server.
nmap <silent> <C-s> <Plug>(coc-range-select)
xmap <silent> <C-s> <Plug>(coc-range-select)

" Add `:Format` command to format current buffer.
command! -nargs=0 Format :call CocAction('format')

" Add `:Fold` command to fold current buffer.
command! -nargs=? Fold :call     CocAction('fold', <f-args>)

" Add `:OR` command for organize imports of the current buffer.
command! -nargs=0 OR   :call     CocAction('runCommand', 'editor.action.organizeImport')

" Add (Neo)Vim's native statusline support.
" NOTE: Please see `:h coc-status` for integrations with external plugins that
" provide custom statusline: lightline.vim, vim-airline.
set statusline^=%{coc#status()}%{get(b:,'coc_current_function','')}

" Mappings for CoCList
" Show all diagnostics.
nnoremap <silent><nowait> <space>a  :<C-u>CocList diagnostics<cr>
" Manage extensions.
nnoremap <silent><nowait> <space>e  :<C-u>CocList extensions<cr>
" Show commands.
nnoremap <silent><nowait> <space>c  :<C-u>CocList commands<cr>
" Find symbol of current document.
nnoremap <silent><nowait> <space>o  :<C-u>CocList outline<cr>
" Search workspace symbols.
nnoremap <silent><nowait> <space>s  :<C-u>CocList -I symbols<cr>
" Do default action for next item.
nnoremap <silent><nowait> <space>j  :<C-u>CocNext<CR>
" Do default action for previous item.
nnoremap <silent><nowait> <space>k  :<C-u>CocPrev<CR>
" Resume latest coc list.
nnoremap <silent><nowait> <space>p  :<C-u>CocListResume<CR>

" copyright
let g:file_copyright_company = "cxysailor-master"
let g:file_copyright_rights = "All rights reserved."
let g:file_copyright_name = "cxysailor"
let g:file_copyright_email = "cxysailor@163.com"
" auto update copyright when save file. Default: 1; 0:close auto.
let g:file_copyright_auto_update = 1
let g:file_copyright_auto_filetypes = ['sh', 'plx', 'pl', 'pm', 'py', 'python','h', 'hpp', 'c', 'cpp', 'java','ruby', 'rb', 'rake','uml', 'plantuml']

" nerdcommenter
" Add spaces after comment delimiters by default
let g:NERDSpaceDelims = 1

" Use compact syntax for prettified multi-line comments
let g:NERDCompactSexyComs = 1

" Align line-wise comment delimiters flush left instead of following code indentation
let g:NERDDefaultAlign = 'left'

" Set a language to use its alternate delimiters by default
let g:NERDAltDelims_java = 1

" Add your own custom formats or override the defaults
let g:NERDCustomDelimiters = { 'c': { 'left': '/**','right': '*/' } }

" Allow commenting and inverting empty lines (useful when commenting a region)
let g:NERDCommentEmptyLines = 1

" Enable trimming of trailing whitespace when uncommenting
let g:NERDTrimTrailingWhitespace = 1

" Enable NERDCommenterToggle to check all selected lines is commented or not 
let g:NERDToggleCheckAllLines = 1

" Powerline
let g:Powerline_symbols = 'fancy'

" tagbar
nmap <F8> :TagbarToggle<CR>

" Bullets.vim
let g:bullets_enabled_file_types = [
    \ 'markdown',
    \ 'text',
    \ 'gitcommit',
    \ 'scratch'
    \]

" nerdtree-devicons-syntax default color
let s:colors = {
  \ 'brown'       : "905532",
  \ 'aqua'        : "3AFFDB",
  \ 'blue'        : "689FB6",
  \ 'darkBlue'    : "44788E",
  \ 'purple'      : "834F79",
  \ 'lightPurple' : "834F79",
  \ 'red'         : "AE403F",
  \ 'beige'       : "F5C06F",
  \ 'yellow'      : "F09F17",
  \ 'orange'      : "D4843E",
  \ 'darkOrange'  : "F16529",
  \ 'pink'        : "CB6F6F",
  \ 'salmon'      : "EE6E73",
  \ 'green'       : "8FAA54",
  \ 'lightGreen'  : "31B53E",
  \ 'white'       : "FFFFFF"
\ }

" vim-indent-guides
let g:indent_guides_enable_on_vim_startup = 1
let g:indent_guides_guide_size = 1
let indent_guides_exclude_filetypes = ['help','nerdtree']
let g:indent_guides_auto_colors = 0
autocmd VimEnter,Colorscheme * :hi IndentGuidesOdd  guibg=red   ctermbg=3
autocmd VimEnter,Colorscheme * :hi IndentGuidesEven guibg=green ctermbg=4

" signature
let g:SignatureMap = {
\ 'Leader' : "m",
\ 'PlaceNextMark' : "m,",
\ 'ToggleMarkAtLine' : "m.",
\ 'PurgeMarksAtLine' : "m-",
\ 'DeleteMark' : "dm",
\ 'PurgeMarks' : "m<Space>",
\ 'PurgeMarkers' : "m<BS>",
\ 'GotoNextLineAlpha' : "']",
\ 'GotoPrevLineAlpha' : "'[",
\ 'GotoNextSpotAlpha' : "`]",
\ 'GotoPrevSpotAlpha' : "`[",
\ 'GotoNextLineByPos' : "]'",
\ 'GotoPrevLineByPos' : "['",
\ 'GotoNextSpotByPos' : "]`",
\ 'GotoPrevSpotByPos' : "[`",
\ 'GotoNextMarker' : "]-",
\ 'GotoPrevMarker' : "[-",
\ 'GotoNextMarkerAny' : "]=",
\ 'GotoPrevMarkerAny' : "[=",
\ 'ListBufferMarks' : "m/",
\ 'ListBufferMarkers' : "m?"
\ }

" Zeavim, Zeal for Vim
nmap gzz <Plug>Zeavim
vmap gzz <Plug>ZVVisSelection
nmap <leader>z <Plug>ZVKeyDocset
nmap gZ <Plug>ZVKeyDocset<CR>
nmap gz <Plug>ZVOperator
let g:zv_keep_focus = 0
let g:zv_file_types = {
            \   'help'                : 'vim',
            \   'javascript'          : 'javascript,nodejs',
            \   'python'              : 'python_3',
            \   '\v^(G|g)ulpfile\.js' : 'gulp,javascript,nodejs',
            \ }
" let g:zv_zeal_args = g:has_unix ? '--style=gtk+' : ''

" online thesaurus
let g:online_thesaurus_map_keys = 0
nnoremap <leader>tk :OnlineThesaurusCurrentWord<CR>

" thesaurus Query
nnoremap <Leader>th :ThesaurusQueryReplaceCurrentWord<CR>
let g:tq_openoffice_en_file="~/.config/nvim/thesaurus/MyThes-1.0/th_en_US_new"
let g:tq_mthesaur_file="~/.config/nvim/thesaurus/mthesaur.txt"
let g:tq_cilin_txt_file="~/.config/nvim/thesaurus/cilin.txt"
let g:tq_enabled_backends=["woxikon_de","jeck_ru","openoffice_en","mthesaur_txt"]
let g:tq_enabled_backends=["cilin_txt",
\"openthesaurus_de",
\"yarn_synsets",
\"openoffice_en",
\"mthesaur_txt",
\"datamuse_com",]

"  fuzzy finder
map <C-p> :FZF<CR>

"  emmet
let g:user_emmet_install_global = 0
autocmd FileType html,css EmmetInstall
let g:user_emmet_leader_key='<C-y>'
" let g:user_emmet_settings = webapi#json#decode(join(readfile(expand('~/.snippets_custom.json')), "\n"))

"  Changing themes
if &t_Co > 2 || has("gui_running")
		set background=dark
		"colorschem dracula
		" colorschem molokai
		"colorschem solarized
		colorschem PaperColor
endif

"  Keys mapping for markdown
"create an anchor quickly
autocmd Filetype markdown inoremap <buffer> <silent> ,, <++> 
"find next anchor
autocmd Filetype markdown inoremap <buffer> <silent> ,f <Esc>/<++><CR>:nohlsearch<CR>c4l
"find next anchor and delete whitespace before anchor
autocmd Filetype markdown inoremap <buffer> <silent> ,s <Esc>/ <++><CR>:nohlsearch<CR>c5l
"seperator
autocmd Filetype markdown inoremap <buffer> <silent> ,- ---<Enter><Enter>
"bold
autocmd Filetype markdown inoremap <buffer> <silent> ,b **** <++><Esc>F*hi
"deletion
autocmd Filetype markdown inoremap <buffer> <silent> ,x ~~~~ <++><Esc>F~hi
"italic
autocmd Filetype markdown inoremap <buffer> <silent> ,i ** <++><Esc>F*i
"code inline
autocmd Filetype markdown inoremap <buffer> <silent> ,q `` <++><Esc>F`i
"code block
autocmd Filetype markdown inoremap <buffer> <silent> ,c ```<Enter><++><Enter>```<Enter><Enter><++><Esc>4kA
"todo
autocmd Filetype markdown inoremap <buffer> <silent> ,g - [ ] <Enter><++><Esc>kA
"underline
autocmd Filetype markdown inoremap <buffer> <silent> ,u <u></u><++><Esc>F/hi
"images
autocmd Filetype markdown inoremap <buffer> <silent> ,p ![](<++>) <++><Esc>F[a
"links
autocmd Filetype markdown inoremap <buffer> <silent> ,a [](<++>) <++><Esc>F[a
"heading 1 - 6
autocmd Filetype markdown inoremap <buffer> <silent> ,1 #<Space><Enter><++><esc>kA
autocmd Filetype markdown inoremap <buffer> <silent> ,2 ##<Space><Enter><++><esc>kA
autocmd Filetype markdown inoremap <buffer> <silent> ,3 ###<Space><Enter><++><esc>kA
autocmd Filetype markdown inoremap <buffer> <silent> ,4 ####<Space><Enter><++><esc>kA
autocmd Filetype markdown inoremap <buffer> <silent> ,5 #####<Space><Enter><++><esc>kA
autocmd Filetype markdown inoremap <buffer> <silent> ,6 ######<Space><Enter><++><esc>kA
"insert current date & time at cursor
autocmd Filetype markdown inoremap <buffer> <silent> ,t <C-R>=strftime("%Y-%m-%d %H:%M:%S")<CR>

"  Compile function
noremap <F5> :call CompileRunGcc()<CR>
func! CompileRunGcc()
    exec "w"
    if &filetype == 'c'
		exec "!g++ % -o %<"
		exec "!time ./%<"
    elseif &filetype == 'cpp'
		set splitbelow
		exec "!g++ -std=c++11 % -Wall -o %<"
		:sp
		:res -15
		:term ./%<
    elseif &filetype == 'java'
		exec "!javac %"
		exec "!time java %<"
    elseif &filetype == 'sh'
		:!time bash %
    elseif &filetype == 'python'
		set splitbelow
		:sp
		:term python3 %
    elseif &filetype == 'html'
		silent! exec "!".g:mkdp_browser." % &"
    elseif &filetype == 'markdown'
		exec "MarkdownPreview"
    elseif &filetype == 'tex'
		silent! exec "VimtexStop"
		silent! exec "VimtexCompile"
    elseif &filetype == 'dart'
		CocCommand flutter.run
    elseif &filetype == 'go'
		set splitbelow
		:sp
		:term go run %
    endif
endfunc
