# Комплексные числа в Python

<!----><span><h2 style="text-align: center;">Комплексные числа в Python</h2>

<p>В языке Python есть возможность работать с комплексными числами. Общая форма представления комплексного числа следующая: <code>real&nbsp;+ imag&nbsp;j</code>, где</p>

<ul>
	<li><code>real</code>&nbsp;– вещественная часть комплексного числа;</li>
	<li><code>imag</code>&nbsp;– мнимая часть комплексного числа, которая завершается символом&nbsp;<code>j</code>&nbsp;или&nbsp;<code>J</code>.</li>
</ul>

<p><img alt="" height="49" src="https://ucarecdn.com/6b13fc82-52cb-4150-8811-90ea780defd8/" width="49">&nbsp; Обратите внимание: в Python используется буква&nbsp;<code>j</code>, а не&nbsp;<code>i</code>.</p>

<p>Приведенный&nbsp;ниже код:</p>

<pre><code class="language-python hljs">z1 = <span class="hljs-number">5</span> + <span class="hljs-number">7j</span>
z2 = <span class="hljs-number">1j</span>
z3 = <span class="hljs-number">-3</span> + <span class="hljs-number">5J</span>
z4 = <span class="hljs-number">1.5</span> + <span class="hljs-number">3.2j</span>

print(z1, z2, z3, z4, sep=<span class="hljs-string">'\n'</span>)
print(type(z1))</code></pre>

<p>выводит:</p>

<pre><code class="language-no-highlight hljs">(5+7j)
1j
(-3+5j)
(1.5+3.2j)
&lt;class 'complex'&gt;</code></pre>

<h3 style="text-align: center;">Создание комплексных чисел</h3>

<p>Комплексные числа можно создать с помощью литерала, как выше, а можно с помощью функции <code>complex()</code>, которая принимает два аргумента: вещественную и мнимую часть числа, либо строковое представление числа.</p>

<p>Приведенный ниже код:</p>

<pre><code class="language-python hljs">z1 = <span class="hljs-number">-3</span> + <span class="hljs-number">2j</span>              <span class="hljs-comment"># создание на основе литерала</span>
z2 = complex(<span class="hljs-number">6</span>, <span class="hljs-number">-8</span>)       <span class="hljs-comment"># z2 = 6 - 8j</span>
z3 = complex(<span class="hljs-number">0</span>, <span class="hljs-number">2.5</span>)      <span class="hljs-comment"># z3 = 2.5j</span>
z4 = complex(<span class="hljs-number">5</span>, <span class="hljs-number">0</span>)        <span class="hljs-comment"># z4 = 5 + 0j</span>
z5 = complex(<span class="hljs-string">'3+4j'</span>)      <span class="hljs-comment"># создание на основе строки</span>

print(z1, z2, z3, z4, z5, sep=<span class="hljs-string">'\n'</span>)</code></pre>

<p>выводит:</p>

<pre><code class="language-no-highlight hljs">(-3+2j)
(6-8j)
2.5j
(5+0j)
(3+4j)</code></pre>

<h3 style="text-align: center;">Арифметические операции над комплексными числами</h3>

<p>Тип данных&nbsp;<code>complex</code>&nbsp;отлично интегрирован в язык Python. С&nbsp;<code>complex</code>&nbsp;числами работают все привычные операции: сложение, вычитание, умножение, деление, возведение в степень.</p>

<p>Приведенный ниже код:</p>

<pre><code class="language-python hljs">z1 = <span class="hljs-number">1</span> + <span class="hljs-number">3j</span>
z2 = <span class="hljs-number">-3</span> + <span class="hljs-number">2j</span>

print(<span class="hljs-string">'z1 + z2 ='</span>, z1 + z2)
print(<span class="hljs-string">'z1 - z2 ='</span>, z1 - z2)
print(<span class="hljs-string">'z1 * z2 ='</span>, z1 * z2)
print(<span class="hljs-string">'z1 / z2 ='</span>, z1 / z2)
print(<span class="hljs-string">'z1^20 ='</span>, z1**<span class="hljs-number">20</span>)</code></pre>

<p>выводит:</p>

<pre><code class="language-python hljs">z1 + z2 = (<span class="hljs-number">-2</span>+<span class="hljs-number">5j</span>)
z1 - z2 = (<span class="hljs-number">4</span>+<span class="hljs-number">1j</span>)
z1 * z2 = (<span class="hljs-number">-9</span><span class="hljs-number">-7j</span>)
z1 / z2 = (<span class="hljs-number">0.23076923076923078</span><span class="hljs-number">-0.8461538461538461j</span>)
z1^<span class="hljs-number">20</span> = (<span class="hljs-number">9884965888</span><span class="hljs-number">-1512431616j</span>)</code></pre>

<p>Мы также можем совершать арифметические операции над&nbsp;<code>complex</code>&nbsp;и&nbsp;целыми числами (миксовать&nbsp;<code>complex</code>,&nbsp;<code>int, float</code>).</p>

<p>Приведенный ниже код:</p>

<pre><code class="language-python hljs">z = <span class="hljs-number">1</span> + <span class="hljs-number">3j</span>

print(z + <span class="hljs-number">5</span>)
print(z - <span class="hljs-number">2</span>)
print(<span class="hljs-number">3</span>*z)
print(z/<span class="hljs-number">2</span>)</code></pre>

<p>выводит:</p>

<pre><code class="language-no-highlight hljs">(6+3j)
(-1+3j)
(3+9j)
(0.5+1.5j)</code></pre>

<h3 style="text-align: center;">Методы и свойства комплексных чисел</h3>

<p>Для получения действительной&nbsp;и мнимой частей комплексного числа&nbsp;используются свойства&nbsp;<code>real</code>&nbsp;и&nbsp;<code>imag</code>.</p>

<p>Приведенный ниже код:</p>

<pre><code class="language-python hljs">z = <span class="hljs-number">3</span>+<span class="hljs-number">4j</span>

print(<span class="hljs-string">'Действительная часть ='</span>, z.real)
print(<span class="hljs-string">'Мнимая часть ='</span>, z.imag)</code></pre>

<p>выводит:</p>

<pre><code class="language-no-highlight hljs">Действительная часть = 3.0
Мнимая часть = 4.0</code></pre>

<p><img alt="" height="49" src="https://ucarecdn.com/ffc99838-c8e5-4d8a-ac8a-21695fa5473a/" style="float: left;" width="49">Python представляет комплексное число как два вещественных числа, поэтому при выводе у нас появились выражения <span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>3.0</mn></mrow><annotation encoding="application/x-tex">3.0</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">3.0</span></span></span></span></span> и <span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>4.0</mn></mrow><annotation encoding="application/x-tex">4.0</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">4.0</span></span></span></span></span> вместо <span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>3</mn></mrow><annotation encoding="application/x-tex">3</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">3</span></span></span></span></span> и <span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>4</mn></mrow><annotation encoding="application/x-tex">4</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">4</span></span></span></span></span>.</p>

<p>Для нахождения сопряженного комплексного числа, можно использовать метод&nbsp;<code>conjugate()</code>.</p>

<p>Приведенный ниже код:</p>

<pre><code class="language-python hljs">z = <span class="hljs-number">3</span>+<span class="hljs-number">4j</span>

print(<span class="hljs-string">'Сопряженное число ='</span>, z.conjugate())</code></pre>

<p>выводит:</p>

<pre><code class="language-no-highlight hljs">Сопряженное число = (3-4j)</code></pre>

<h2 style="text-align: center;">Примечания</h2>

<p><strong>Примечание 1.</strong> Почему используется буква <code>j</code> вместо буквы <code>i</code>, можно почитать <a href="https://stackoverflow.com/questions/24812444/why-are-complex-numbers-in-python-denoted-with-j-instead-of-i" rel="noopener noreferrer nofollow" target="_blank">тут</a>.</p>

<p><strong>Примечание 2.</strong> Для нахождения модуля комплексного числа, используется встроенная функция <code>abs()</code>.</p>

<p>Приведенный ниже код:</p>

<pre><code class="language-python hljs">z = <span class="hljs-number">3</span>+<span class="hljs-number">4j</span>

print(<span class="hljs-string">'Модуль числа ='</span>, abs(z))</code></pre>

<p>выводит:</p>

<pre><code class="language-no-highlight hljs">Модуль числа = 5.0</code></pre>

<p><strong>Примечание 3. </strong>Встроенный модуль <code>math</code>&nbsp;работает с вещественными числами. Для работы с комплексными числами есть модуль <code>cmath</code>.&nbsp;Модуль&nbsp;<code>cmath</code>&nbsp;включает дополнительные функции для использования комплексных чисел.</p>

<pre><code class="language-python hljs"><span class="hljs-keyword">import</span> cmath

z = <span class="hljs-number">2</span>+<span class="hljs-number">3j</span>
print(cmath.phase(z)) <span class="hljs-comment"># полярный угол</span>
print(cmath.polar(z)) <span class="hljs-comment"># полярные координаты</span></code></pre>

<p>Модуль <code>cmath</code> содержит следующие категории функций:</p>

<ul>
	<li>
	<p>Экспоненциальные и логарифмические функции</p>
	</li>
</ul>

<ul>
	<li>
	<p>Квадратные корни</p>
	</li>
	<li>
	<p>Тригонометрические функции и их обратные</p>
	</li>
	<li>
	<p>Гиперболические функции и их обратные</p>
	</li>
</ul>

<p><strong>Примечание 4.</strong> Документация по модулю <code>cmath</code> <a href="https://docs.python.org/3/library/cmath.html" rel="noopener noreferrer nofollow" target="_blank">тут</a>.</p>

<p><strong>Примечание 5.</strong> Больше примеров работы с комплексными числами <a href="https://www.askpython.com/python/python-complex-numbers" rel="noopener noreferrer nofollow" target="_blank">тут</a>.</p>

<p><strong>Примечание 6.</strong> Для работы с комплексными числами (тип <code>complex</code>) не нужно подключать какой-либо модуль, в&nbsp;отличии от типа <code>Decimal</code> и <code>Fraction</code>.</p>

<h2 style="text-align: right;"><strong>Made with&nbsp;💛 by&nbsp;BEEGEEK</strong></h2></span>
