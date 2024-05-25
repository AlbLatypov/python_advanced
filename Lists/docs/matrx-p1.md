# Матрицы. Часть 1

<!----><span><h1>Тема урока: матрицы</h1>

<ol>
	<li>Работа с матрицами</li>
	<li>Квадратные и прямоугольные матрицы</li>
	<li>Функции <code>ljust()</code> и <code>rjust()</code></li>
	<li>Главная и побочная диагонали</li>
</ol>

<p><strong>Аннотация.</strong>&nbsp;Урок посвящен работе с матрицами — прямоугольными таблицами.</p>

<h2 style="text-align: center;">Матрицы</h2>

<p>В прошлых уроках&nbsp;мы изучили&nbsp;<strong>вложенные списки</strong>, то есть списки, входящие в качестве элементов в другие списки. Частный&nbsp;случай вложенных списков —&nbsp;матрицы. Это прямоугольные таблицы, заполненные&nbsp;какими-то значениями, обычно числами.</p>

<p style="text-align: center;"><img alt="" height="311" name="image.png" src="https://ucarecdn.com/8fc2bdde-1f71-4061-9641-b94a7276b55e/" width="375"></p>

<p><img alt="" height="49" src="https://ucarecdn.com/462c76a3-9931-488d-b3da-43867e8a293a/" style="float: left;" width="49">Матрицы часто применяются в математике, так как многие задачи с&nbsp;их&nbsp;помощью гораздо проще сформулировать, записать и&nbsp;решить.</p>

<p>Для&nbsp;работы с матрицами нужно уметь получать элемент&nbsp;<span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>i</mi></mrow><annotation encoding="application/x-tex">i</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.65952em; vertical-align: 0em;"></span><span class="mord mathnormal">i</span></span></span></span></span>-й строки&nbsp;<span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>j</mi></mrow><annotation encoding="application/x-tex">j</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.85396em; vertical-align: -0.19444em;"></span><span style="margin-right: 0.05724em;" class="mord mathnormal">j</span></span></span></span></span>-го столбца. Для этого обычно заводят список строк матрицы, где&nbsp;каждая строка — список&nbsp;элементов. Получается вложенный список или&nbsp;список списков. Теперь, чтобы получить определенный элемент,&nbsp;достаточно из&nbsp;списка строк матрицы выбрать <span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>i</mi></mrow><annotation encoding="application/x-tex">i</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.65952em; vertical-align: 0em;"></span><span class="mord mathnormal">i</span></span></span></span></span>-ю и&nbsp;взять <span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>j</mi></mrow><annotation encoding="application/x-tex">j</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.85396em; vertical-align: -0.19444em;"></span><span style="margin-right: 0.05724em;" class="mord mathnormal">j</span></span></span></span></span>-й элемент этой строки.</p>

<p>Давайте заведем&nbsp;матрицу&nbsp;размера <span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>3</mn><mo>×</mo><mn>4</mn></mrow><annotation encoding="application/x-tex">3 \times 4</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.72777em; vertical-align: -0.08333em;"></span><span class="mord">3</span><span class="mspace" style="margin-right: 0.222222em;"></span><span class="mbin">×</span><span class="mspace" style="margin-right: 0.222222em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">4</span></span></span></span></span>&nbsp;(<span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>3</mn></mrow><annotation encoding="application/x-tex">3</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">3</span></span></span></span></span> строки и <span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>4</mn></mrow><annotation encoding="application/x-tex">4</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">4</span></span></span></span></span> столбца), содержащую числа, и&nbsp;получим элемент на&nbsp;позиции <span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">(</mo><mn>2</mn><mo separator="true">,</mo><mtext>&nbsp;</mtext><mn>3</mn><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">(2,&nbsp;3)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mopen">(</span><span class="mord">2</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.166667em;"></span><span class="mord">&nbsp;3</span><span class="mclose">)</span></span></span></span></span>, то есть элемент второй строки в&nbsp;третьем столбце.</p>

<pre><code class="language-python hljs">matrix  = [[<span class="hljs-number">2</span>, <span class="hljs-number">-5</span>, <span class="hljs-number">-11</span>, <span class="hljs-number">0</span>],
           [<span class="hljs-number">-9</span>, <span class="hljs-number">4</span>, <span class="hljs-number">6</span>, <span class="hljs-number">13</span>],
           [<span class="hljs-number">4</span>, <span class="hljs-number">7</span>, <span class="hljs-number">12</span>, <span class="hljs-number">-2</span>]]

print(matrix[<span class="hljs-number">1</span>][<span class="hljs-number">2</span>])  <span class="hljs-comment"># вывод элемента на позиции (2, 3)</span>
</code></pre>

<p>В переменной <code>matrix</code>&nbsp;хранится вся матрица, при этом&nbsp;<code>matrix[1]</code>&nbsp;— список значений во второй&nbsp;строке,&nbsp;<code>matrix[1][2]</code>&nbsp;— элемент в&nbsp;третьем столбце&nbsp;этой строки.</p>

<p style="text-align: center;"><img alt="" height="275" name="image.png" src="https://ucarecdn.com/c29bce90-65bf-46df-8cd5-60dbcb06e9f8/" width="524"></p>

<p><img alt="" height="50" src="https://ucarecdn.com/dea2afa5-6ab3-473c-96af-bc79facae05d/" style="float: left;" width="50">В&nbsp;математике нумерация строк и&nbsp;столбцов начинается&nbsp;с&nbsp;единицы, а&nbsp;не&nbsp;с&nbsp;нуля. По&nbsp;договоренности&nbsp;сначала всегда указывается строка, а затем&nbsp;— столбец. Элемент на <span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>i</mi></mrow><annotation encoding="application/x-tex">i</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.65952em; vertical-align: 0em;"></span><span class="mord mathnormal">i</span></span></span></span></span>-ой строке, <span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>j</mi></mrow><annotation encoding="application/x-tex">j</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.85396em; vertical-align: -0.19444em;"></span><span style="margin-right: 0.05724em;" class="mord mathnormal">j</span></span></span></span></span>-м столбце матрицы <span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>a</mi></mrow><annotation encoding="application/x-tex">a</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathnormal">a</span></span></span></span></span> обозначается так – <span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub></mrow><annotation encoding="application/x-tex">a_{ij}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.716668em; vertical-align: -0.286108em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.311664em;"><span class="" style="top: -2.55em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span style="margin-right: 0.05724em;" class="mord mathnormal mtight">ij</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.286108em;"><span class=""></span></span></span></span></span></span></span></span></span></span>.</p>

<h2 style="text-align: center;">Перебор элементов матрицы</h2>

<p>Чтобы перебрать элементы матрицы, необходимо использовать <strong>вложенные&nbsp;циклы</strong>. Например, выведем на&nbsp;экран все элементы матрицы, <strong>перебирая их&nbsp;по строкам</strong>:</p>

<pre><code class="language-python hljs">rows, cols = <span class="hljs-number">3</span>, <span class="hljs-number">4</span>  <span class="hljs-comment"># rows - количество строк, cols - количество столбцов</span>

matrix  = [[<span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">1</span>, <span class="hljs-number">0</span>],
           [<span class="hljs-number">9</span>, <span class="hljs-number">4</span>, <span class="hljs-number">6</span>, <span class="hljs-number">8</span>],
           [<span class="hljs-number">4</span>, <span class="hljs-number">7</span>, <span class="hljs-number">2</span>, <span class="hljs-number">7</span>]]

<span class="hljs-keyword">for</span> r <span class="hljs-keyword">in</span> range(rows):
    <span class="hljs-keyword">for</span> c <span class="hljs-keyword">in</span> range(cols):
        print(matrix[r][c], end=<span class="hljs-string">' '</span>)
    print()</code></pre>

<p>Результатом работы такого кода будет:</p>

<pre><code class="language-no-highlight hljs">2 3 1 0 
9 4 6 8 
4 7 2 7 </code></pre>

<p>Для перебора элементов матрицы <strong>по столбцам</strong> можно использовать следующий код:</p>

<pre><code class="language-python hljs">rows, cols = <span class="hljs-number">3</span>, <span class="hljs-number">4</span>  <span class="hljs-comment"># rows - количество строк, cols - количество столбцов</span>

matrix  = [[<span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">1</span>, <span class="hljs-number">0</span>],
           [<span class="hljs-number">9</span>, <span class="hljs-number">4</span>, <span class="hljs-number">6</span>, <span class="hljs-number">8</span>],
           [<span class="hljs-number">4</span>, <span class="hljs-number">7</span>, <span class="hljs-number">2</span>, <span class="hljs-number">7</span>]]

<span class="hljs-keyword">for</span> c <span class="hljs-keyword">in</span> range(cols):
    <span class="hljs-keyword">for</span> r <span class="hljs-keyword">in</span> range(rows):
        print(matrix[r][c], end=<span class="hljs-string">' '</span>)
    print()</code></pre>

<p>Результатом работы такого кода будет:</p>

<pre><code class="language-no-highlight hljs">2 9 4 
3 4 7 
1 6 2 
0 8 7</code></pre>

<h2 style="text-align: center;">Функции ljust() и rjust()</h2>

<p>Рассмотрим программный код:</p>

<pre><code class="language-python hljs">rows, cols = <span class="hljs-number">3</span>, <span class="hljs-number">4</span>  <span class="hljs-comment"># rows - количество строк, cols - количество столбцов</span>

matrix  = [[<span class="hljs-number">277</span>, <span class="hljs-number">-930</span>, <span class="hljs-number">11</span>, <span class="hljs-number">0</span>],
           [<span class="hljs-number">9</span>, <span class="hljs-number">43</span>, <span class="hljs-number">6</span>, <span class="hljs-number">87</span>],
           [<span class="hljs-number">4456</span>, <span class="hljs-number">8</span>, <span class="hljs-number">290</span>, <span class="hljs-number">7</span>]]

<span class="hljs-keyword">for</span> r <span class="hljs-keyword">in</span> range(rows):
    <span class="hljs-keyword">for</span> c <span class="hljs-keyword">in</span> range(cols):
        print(matrix[r][c], end=<span class="hljs-string">' '</span>)
    print()</code></pre>

<p>&nbsp;Результатом работы такого кода будет:</p>

<pre><code class="language-no-highlight hljs">277 -930 11 0 
9 43 6 87 
4456 8 290 7 </code></pre>

<p>Выведенная матрица не сильно похожа на упорядоченный прямоугольник. Элементы матрицы имеют разное количество разрядов и результат вывода&nbsp;получается смазанным. Для решения&nbsp;проблемы удобно использовать&nbsp;строковые методы <code>ljust()</code> и <code>rjust()</code>.</p>

<h3 style="text-align: center;">Метод ljust()</h3>

<p>Строковый метод <code>ljust()</code>&nbsp;выравнивает текст по ширине, <strong>добавляя пробелы</strong> в конец текста.</p>

<p>Результатом выполнения следующего кода:</p>

<pre><code class="language-python hljs">print(<span class="hljs-string">'a'</span>.ljust(<span class="hljs-number">3</span>))
print(<span class="hljs-string">'ab'</span>.ljust(<span class="hljs-number">3</span>))
print(<span class="hljs-string">'abc'</span>.ljust(<span class="hljs-number">3</span>))</code></pre>

<p>будет:</p>

<pre><code class="language-no-highlight hljs">a⎵⎵
ab⎵
abc</code></pre>

<p>Исходная строка не обрезается, даже если в ней больше символов, чем нужно.</p>

<p>Результатом выполнения следующего кода:</p>

<pre><code class="language-python hljs">print(<span class="hljs-string">'abcdefg'</span>.ljust(<span class="hljs-number">3</span>))</code></pre>

<p>будет:</p>

<pre><code class="language-no-highlight hljs">abcdefg</code></pre>

<p>Строковый метод&nbsp;<code>ljust()</code>&nbsp;использует вместо пробела другой символ, если передать ему второй аргумент, необязательный.</p>

<p>Результатом выполнения следующего кода:</p>

<pre><code class="language-python hljs">print(<span class="hljs-string">'a'</span>.ljust(<span class="hljs-number">5</span>, <span class="hljs-string">'*'</span>))
print(<span class="hljs-string">'ab'</span>.ljust(<span class="hljs-number">5</span>, <span class="hljs-string">'$'</span>))
print(<span class="hljs-string">'abc'</span>.ljust(<span class="hljs-number">5</span>, <span class="hljs-string">'#'</span>))</code></pre>

<p>будет:</p>

<pre><code class="language-no-highlight hljs">a****
ab$$$
abc##</code></pre>

<h3 style="text-align: center;">Метод rjust()</h3>

<p>Строковый метод <code>rjust()</code>&nbsp;выравнивает текст по ширине, <strong>добавляя пробелы</strong> в начало&nbsp;текста.</p>

<p>Результатом выполнения следующего кода:</p>

<pre><code class="language-python hljs">print(<span class="hljs-string">'a'</span>.rjust(<span class="hljs-number">3</span>))
print(<span class="hljs-string">'ab'</span>.rjust(<span class="hljs-number">3</span>))
print(<span class="hljs-string">'abc'</span>.rjust(<span class="hljs-number">3</span>))</code></pre>

<p>будет:</p>

<pre><code class="language-no-highlight hljs">⎵⎵a
⎵ab
abc</code></pre>

<p>Исходная строка не обрезается, даже если в ней больше символов, чем нужно.</p>

<p>Результатом выполнения следующего кода:</p>

<pre><code class="language-python hljs">print(<span class="hljs-string">'abcdefg'</span>.rjust(<span class="hljs-number">3</span>))</code></pre>

<p>будет:</p>

<pre><code class="language-no-highlight hljs">abcdefg</code></pre>

<p>Строковый метод&nbsp;<code>rjust()</code>&nbsp;использует вместо пробела другой символ, если передать ему второй аргумент, необязательный.</p>

<p>Результатом выполнения следующего кода:</p>

<pre><code class="language-python hljs">print(<span class="hljs-string">'a'</span>.rjust(<span class="hljs-number">5</span>, <span class="hljs-string">'*'</span>))
print(<span class="hljs-string">'ab'</span>.rjust(<span class="hljs-number">5</span>, <span class="hljs-string">'$'</span>))
print(<span class="hljs-string">'abc'</span>.rjust(<span class="hljs-number">5</span>, <span class="hljs-string">'#'</span>))</code></pre>

<p>будет:</p>

<pre><code class="language-no-highlight hljs">****a
$$$ab
##abc</code></pre>

<p>Применив метод <code>ljust()</code> для выравнивания столбцов, при выводе таблицы мы получим следующий код:</p>

<pre><code class="language-python hljs">rows, cols = <span class="hljs-number">3</span>, <span class="hljs-number">4</span>  <span class="hljs-comment"># rows - количество строк, cols - количество столбцов</span>

matrix  = [[<span class="hljs-number">277</span>, <span class="hljs-number">-930</span>, <span class="hljs-number">11</span>, <span class="hljs-number">0</span>],
           [<span class="hljs-number">9</span>, <span class="hljs-number">43</span>, <span class="hljs-number">6</span>, <span class="hljs-number">87</span>],
           [<span class="hljs-number">4456</span>, <span class="hljs-number">8</span>, <span class="hljs-number">290</span>, <span class="hljs-number">7</span>]]

<span class="hljs-keyword">for</span> r <span class="hljs-keyword">in</span> range(rows):
    <span class="hljs-keyword">for</span> c <span class="hljs-keyword">in</span> range(cols):
        print(str(matrix[r][c]).ljust(<span class="hljs-number">6</span>), end=<span class="hljs-string">''</span>)
    print()</code></pre>

<p>Результатом выполнения такого кода будет:</p>

<pre><code class="language-no-highlight hljs">277   -930  11    0     
9     43    6     87    
4456  8     290   7     </code></pre>

<h2 style="text-align: center;">Квадратные матрицы</h2>

<p>Матрица с&nbsp;одинаковым&nbsp;количеством строк и столбцов&nbsp;называется&nbsp;<strong>квадратной</strong>. У квадратной матрицы есть две диагонали:</p>

<ul>
	<li><strong>главная</strong>:&nbsp;проходит из верхнего левого&nbsp;в правый&nbsp;нижний угол&nbsp;матрицы;</li>
	<li><strong>побочная</strong>:&nbsp;проходит из нижнего левого&nbsp;в правый верхний угол&nbsp;матрицы.</li>
</ul>

<p style="text-align: center;"><img alt="" height="254" name="image.png" src="https://ucarecdn.com/9bf38106-5f66-4851-84e8-dd8fd30b5092/" width="707"></p>

<p>Элементы с равными&nbsp;индексами&nbsp;<code>i == j</code>&nbsp;находятся на&nbsp;<strong>главной диагонали</strong>. Такие&nbsp;элементы обозначаются <code>matrix[i][i]</code>.</p>

<p>Элементы с индексами&nbsp;<code>i</code> и <code>j</code>, связанными соотношением <code>i + j + 1 = n</code>&nbsp;(или <code>j = n - i - 1</code>),&nbsp;где <code>n</code> —&nbsp;размерность матрицы, находятся на <strong>побочной диагонали</strong>.</p>

<p>Таким образом, чтобы установить элементы главной или побочной диагонали,&nbsp;достаточно одного цикла.</p>

<p>Результатом выполнения следующего кода:</p>

<pre><code class="language-python hljs">n = <span class="hljs-number">8</span>
matrix = [[<span class="hljs-number">0</span>]*n <span class="hljs-keyword">for</span> _ <span class="hljs-keyword">in</span> range(n)]    <span class="hljs-comment"># создаем квадратную матрицу размером 8×8</span>

<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(n):                    <span class="hljs-comment"># заполняем главную диагональ единицами, а побочную двойками</span>
    matrix[i][i] = <span class="hljs-number">1</span>
    matrix[i][n-i<span class="hljs-number">-1</span>] = <span class="hljs-number">2</span>

<span class="hljs-keyword">for</span> r <span class="hljs-keyword">in</span> range(n):                    <span class="hljs-comment"># выводим матрицу</span>
    <span class="hljs-keyword">for</span> c <span class="hljs-keyword">in</span> range(n):
        print(matrix[r][c], end=<span class="hljs-string">' '</span>)
    print()</code></pre>

<p>будет:</p>

<pre><code class="language-no-highlight hljs">1 0 0 0 0 0 0 2 
0 1 0 0 0 0 2 0 
0 0 1 0 0 2 0 0 
0 0 0 1 2 0 0 0 
0 0 0 2 1 0 0 0 
0 0 2 0 0 1 0 0 
0 2 0 0 0 0 1 0 
2 0 0 0 0 0 0 1 </code></pre>

<p><img alt="" height="67" src="https://ucarecdn.com/8f2f250b-a7bf-44bf-afaa-5f2020e93f23/" style="float: left;" width="67">Индексы<code>i</code> и <code>j</code>элементов&nbsp;на главной&nbsp;диагонали&nbsp;связаны соотношением <code>i = j</code>.&nbsp;Индексы <code>i</code> и <code>j</code>элементов&nbsp;на побочной диагонали&nbsp;связаны соотношением <code>i +&nbsp;j + 1 = n</code>&nbsp;(или&nbsp;&nbsp;<code>j = n - i&nbsp;- 1</code>), где <code>n</code> —&nbsp;размерность матрицы.</p>

<p>Заметим также, что:</p>

<ul>
	<li>если элемент находится выше главной диагонали, то&nbsp;<code>i &lt; j</code>, если ниже -&nbsp;<code>i &gt; j</code>.</li>
	<li>если элемент находится выше побочной диагонали, то&nbsp;<code>i + j + 1 &lt; n</code>, если ниже -&nbsp;<code>i + j + 1 &gt; n</code>.</li>
</ul>

<h2 style="text-align: center;">Примечания</h2>

<p><strong>Примечание 1.</strong> Чтобы понять, в какой области лежит элемент можно воспользоваться следующей картинкой.</p>

<p style="text-align: center;"><img alt="" height="300" name="image.png" src="https://ucarecdn.com/dc096525-602a-4090-8b85-1ce7d851290f/" width="302"></p>

<p><strong>Примечание 2.</strong> Используйте функцию <code>print_matrix()</code> для вывода квадратной&nbsp;матрицы размерности <code>n</code>:</p>

<pre><code class="language-python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print_matrix</span><span class="hljs-params">(matrix, n, width=<span class="hljs-number">1</span>)</span>:</span>
    <span class="hljs-keyword">for</span> r <span class="hljs-keyword">in</span> range(n):
        <span class="hljs-keyword">for</span> c <span class="hljs-keyword">in</span> range(n):
            print(str(matrix[r][c]).ljust(width), end=<span class="hljs-string">' '</span>)
        print()</code></pre>

<p><strong>Примечание 3.</strong> Для считывания матрицы из&nbsp;<code>n</code>&nbsp;строк, заполненной числами, удобно использовать следующий код:</p>

<pre><code class="language-python hljs">n = int(input())
matrix = []
<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(n):
    temp = [int(num) <span class="hljs-keyword">for</span> num <span class="hljs-keyword">in</span> input().split()]
    matrix.append(temp)</code></pre>

<h2 style="text-align: right;"><strong>Made with&nbsp;💛 by&nbsp;BEEGEEK</strong></h2></span>
