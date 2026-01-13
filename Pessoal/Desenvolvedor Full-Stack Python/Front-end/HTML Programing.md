
## HTML

- Linguagem de Marcação
- Sintaxe
- Estrutura de Elementos
- Interpretados pelo Navegador
- Tags `<html></html>`

## Sintaxe

- Estrutura
- Padrões
- `<head>`
- `<!DOCTYPE html>`
- `<body>`
- Tags + attr


![](../IMG/Captura%20de%20tela%20de%202026-01-12%2021-35-23.png)

## Listas e Links

- Listagem
- Agrupamento
- Navegação
- Descrição
- Interação

## Formatação de Textos

- Destaque
- Hierarquia
- Semântica
- Legibilidade

## Tabelas

- Organização
- Apresentação de dados
- Estrutura
- Layout
- Diagramação

## Code Together

- Layout
- Planejamento
- Codificação
- Teste
- Envio

### Introdução

```
<!DOCTYPE html>
<html lang="pt_BR">
	<head>
		<title>Título da página exibido no navegador</title>
	</head>
	<body>
		<h1>Título exibido no corpo html</h1>
		<p>qualquer texto sem marcação ... </p>
	</body>
</html>
```

### Listas e Links

```
<!DOCTYPE html>
<html lang="pt-br">
	<head>
		<title>HTML - Listas e Links</title>
		<meta charset="UTF-8">
	</head>
	<body>
		<h1>Listas e Links</h1>

		<h2 id="lista-nao-ordenada">Lista não ordenada</h2>
		
		<ul>
			<li>
				Brasil
				<ul>
					<li>São Paulo
						<ol>
							<li>São Paulo</li>
						</ol>
					</li>
					<li>Rio de Janeiro</li>
					<li>Minas Gerais</li>
					<li>Pará
						<ul>
							<li>Belém</li>
						</ul>
					</li>
				</ul>
			</li>
			<li>Argentina</li>
			<li>Uruguai</li>
			<li>Paraguai</li>
		</ul>

		<h2>Lista ordenada</h2>

		<ol>
			<li>Corinthians</li>
			<li>Palmeiras</li>
			<li>Santos</li>
			<li>São Paulo</li>
		</ol>

		
		<h2>Lista de Definições</h2>		

		<dl>
			<dt>TV</dt>
				<dd>32 polegadas, smart, ...</dd>
				<dd>127 volts</dd>
			<dt>PC</dt>
				<dd>USB, 19 polegadas, Core I5</dd>
		</dl>

		<h2>Links</h2>

		<nav>
			<ul>
				<li><a href="https://google.com">EBAC</a></li>
				<li><a href="#top">Voltar ao topo</a> </li>
				<li><a href="#lista-nao-ordenada">Ver a lista não ordenada</a></li>
			</ul>
		</nav>

	</body>
</html>
```

### Formatação

```
<!DOCTYPE html>
<html lang="pt-br">
	<head>
		<title>HTML - Formatação de Texto</title>
		<meta charset="UTF-8">
	</head>
	<body>
		<h1>Formatação de Texto</h1>
		<h2>Cabeçalho 2</h2>
		<h3>Título 3</h3>
		<h4>Título 4</h4>
		<h5>Título 5</h5>
		<h6>Título 6</h6>

		<p> <b>Lorem ipsum dolor sit amet</b>, <i>consectetur adipiscing elit</i>. <del>Morbi tempus tortor mollis pellentesque consectetur</del>. Pellentesque non lacus sagittis, venenatis nulla eget, bibendum sem. Mauris ornare, est eget egestas aliquet, lectus purus aliquet est, ut tempus ante nulla sit amet diam. Ut a nunc sit amet tortor ornare vulputate a nec nunc. Vivamus et porttitor ligula. Suspendisse potenti. Vestibulum scelerisque vestibulum condimentum. Nam fermentum, tellus vitae imperdiet consequat, diam ligula fermentum nisl, sed varius arcu risus nec sem. Cras gravida eget ante et suscipit. Ut commodo elit purus, at sagittis orci porttitor eu. Praesent tristique interdum eleifend.</p>

		<p> <strong>Cras venenatis consectetur massa</strong>, <em>ac sodales massa tincidunt vel. Integer consectetur mauris tortor</em> <sup>1</sup>, ac elementum lacus congue sed<sup>2</sup>. Nunc nisl justo, vehicula lobortis erat ac, malesuada iaculis ligula<sub>3</sub>. Fusce blandit id nulla vel pretium. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. <br> <small>Maecenas sed dictum tellus. Sed auctor laoreet sapien, sed posuere massa porttitor eget. Aliquam tristique purus vel nisi accumsan, eget aliquam ex pulvinar. Mauris sollicitudin nunc eu urna dapibus ultricies. Cras lobortis neque libero, at efficitur mauris feugiat eget. Nam non maximus augue. Nullam eget lacinia massa. In dignissim est eu metus finibus condimentum. Aenean velit urna, bibendum vitae aliquam a, bibendum ac quam. Duis fermentum nunc et volutpat egestas</small>.</p>

		<blockquote>"Curabitur dapibus ultrices turpis, at gravida dolor hendrerit sit amet. Quisque non fermentum diam, in ornare lacus. Sed tristique suscipit dapibus. Maecenas non mi risus. Etiam pretium velit et turpis aliquet tristique. Quisque ac leo ligula. Aliquam volutpat, dolor quis mollis volutpat, nulla quam bibendum nunc, ut elementum nulla felis eu tellus. Mauris et odio sapien. Mauris vestibulum elit ut erat volutpat gravida. Duis vulputate erat in eros molestie ultrices. In nec enim ullamcorper, volutpat quam sit amet, sollicitudin odio. Aenean imperdiet quis felis quis semper. Suspendisse dignissim mauris non enim vestibulum tincidunt. Donec mollis tempus venenatis. Nam eu odio velit."</blockquote>



	</body>
</html>
```

### Tabelas

```
<!DOCTYPE html>
<html lang="pt-br">
	<head>
		<title>HTML - Tabelas</title>
		<meta charset="UTF-8">
	</head>
	<body>

		<h1>Tabelas</h1>

		<table border="1" width="100%">
			<thead>
				<tr>
					<th>Coluna 1</th>
					<th>Coluna 2</th>
					<th>Coluna 3</th>
				</tr>
			</thead>
			<tbody>	
				<tr align="center">
					<td>1A</td>
					<td>1B</td>
					<td>1C</td>
				</tr>
				<tr align="right">
					<td>2A</td>
					<td>2B</td>
					<td>2C</td>
				</tr>
				<tr>
					<td>3A</td>
					<td colspan="2">3BC</td>
				</tr>
			</tbody>
			<tfoot>
				<tr>
					<td colspan="3">Rodapé da tabela</td>
				</tr>
			</tfoot>
		</table>


		<h2>Tabela como layout</h2>

		<table width="600">
			<tr height="90">
				<td colspan="4" bgcolor="#BBCCEE" align="center"> Cabeçalho</td>
			</tr>
			<tr height="300">
				<td width="20" bgcolor="#0000FF"></td>
				<td width="60%" bgcolor="#DDDDDD">
					<h2>Título</h2>
					<p>fdajfkdj jfdjfodsapodhgdo odihofdfhsdooi</p>

				</td>
				<td bgcolor="#EEEEEE">Coluna 2</td>
				<td width="20"bgcolor="#0000FF"></td>
			</tr>
			<tr>
				<td bgcolor="#FF0000" colspan="4" align="center">Rodapé</td>
			</tr>
		</table>

	</body>
</html>
```

### Layouts

```
<!DOCTYPE html>
<html lang="pt-br">
	<head>
		<title>HTML - Layouts</title>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<style>
			* {
			  box-sizing: border-box;
			}

			body {
			  font-family: Arial, Helvetica, sans-serif;
			}

			/* Style the header */
			header {
			  background-color: #666;
			  padding: 30px;
			  text-align: center;
			  font-size: 35px;
			  color: white;
			}

			/* Create two columns/boxes that floats next to each other */
			nav {
			  float: left;
			  width: 30%;
			   
			  background: #ccc;
			  padding: 20px;
			}

			/* Style the list inside the menu */
			nav ul {
			  list-style-type: none;
			  padding: 0;
			}

			article {
			  float: left;
			  padding: 20px;
			  width: 70%;
			  background-color: #f1f1f1;
			}

			/* Clear floats after the columns */
			section::after {
			  background: #ccc;
			  content: "";
			  display: table;
			  clear: both;
			}

			/* Style the footer */
			footer {
			  background-color: #777;
			  padding: 10px;
			  text-align: center;
			  color: white;
			}

			/* Responsive layout - makes the two columns/boxes stack on top of each other instead of next to each other, on small screens */
			@media (max-width: 600px) {
			  nav, article {
			    width: 100%;
			    height: auto;
			  }
			}
			</style>
	</head>
	<body>

		<header>
			<h2>Curso Front-end - HTML</h2>
		</header>

		<section>

			<nav>
				<ul>
					<li><a href="#home">Home</a></li>
					<li><a href="#sobre">Sobre</a></li>
					<li><a href="./06-formularios.html">Contato</a></li>
				</ul>
			</nav>

			<article>

				<h1>Título Artigo</h1>

				<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam id nibh posuere, eleifend lacus quis, blandit mauris. Proin eu gravida justo. Donec a mi laoreet, malesuada est a, imperdiet leo. Fusce in mauris dapibus, cursus purus vitae, pulvinar ligula. Donec nec mi mollis, viverra purus et, faucibus ante. Fusce faucibus pretium eros, vitae condimentum orci dapibus eu. Morbi elit nibh, pulvinar ut laoreet sit amet, dignissim id lectus. Nunc ac felis posuere, interdum eros vitae, sodales eros. Aenean porta vehicula diam, sit amet venenatis ante eleifend in. Integer malesuada urna nunc, dapibus dapibus felis malesuada et. Ut id tempor dolor, ac imperdiet lorem. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque risus quam, mollis in tellus quis, blandit venenatis nunc.</p>

				<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nullam sit amet ullamcorper odio. Etiam dignissim arcu vel porta dictum. Proin vel maximus justo, quis rutrum lectus. Nullam pellentesque id enim quis imperdiet. Aenean condimentum ultricies ex vitae auctor. Proin condimentum congue felis, nec aliquet erat tempus ut. Phasellus quis molestie nulla, tincidunt finibus tortor. Aliquam nulla erat, tristique at pharetra eget, vestibulum a diam. Maecenas aliquet porta elit et pretium. In sed ante nibh. Nulla facilisi. Curabitur finibus gravida lacus, eu vestibulum ex. Morbi nec suscipit felis.</p>
				
			</article>


		</section>

		<footer>
			<p>Desenvolvido por Pablo</p>
		</footer>
		
	</body>
</html>
```

### Formularios

```
<!DOCTYPE html>
<html lang="pt-br">
	<head>
		<title>HTML - Formulário Fale Conosco</title>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<style>
			* {
			  box-sizing: border-box;
			}

			body {
			  font-family: Arial, Helvetica, sans-serif;
			}

			/* Style the header */
			header {
			  background-color: #666;
			  padding: 30px;
			  text-align: center;
			  font-size: 35px;
			  color: white;
			}

			/* Create two columns/boxes that floats next to each other */
			nav {
			  float: left;
			  width: 30%;
			   
			  background: #ccc;
			  padding: 20px;
			}

			/* Style the list inside the menu */
			nav ul {
			  list-style-type: none;
			  padding: 0;
			}

			article {
			  float: left;
			  padding: 20px;
			  width: 70%;
			  background-color: #f1f1f1;
			}

			/* Clear floats after the columns */
			section::after {
			  background: #ccc;
			  content: "";
			  display: table;
			  clear: both;
			}

			/* Style the footer */
			footer {
			  background-color: #777;
			  padding: 10px;
			  text-align: center;
			  color: white;
			}

			/* Responsive layout - makes the two columns/boxes stack on top of each other instead of next to each other, on small screens */
			@media (max-width: 600px) {
			  nav, article {
			    width: 100%;
			    height: auto;
			  }
			}
			</style>
	</head>
	<body>

		<header>
			<h2>Curso Front-end - HTML</h2>
		</header>

		<section>

			<nav>
				<ul>
					<li><a href="05-layouts.html">Home</a></li>
					<li><a href="#sobre">Sobre</a></li>
					<li><a href="#contato">Contato</a></li>
				</ul>
			</nav>

			<article>

				<h1>Contato</h1>
				<p>Preencha os campos abaixo</p>

				<form method="post">

					<div>
						<label for="nome">Nome</label><br>
						<input type="text" name="nome" id="nome" placeholder="Digite seu nome">
					</div>

					<div>
						<label for="email">E-mail</label><br>
						<input type="email" name="email" id="email" placeholder="Digite seu email">
					</div>

					<div>
						<label for="mensagem">Mensagem</label><br>
						<textarea name="mensagem" id="mensagem" rows="5"></textarea>
					</div>

					<div>
						<p>
							<label>Qual linguagem você prefere?</label>
							<input type="radio" name="linguagens" value="html"> HTML
							<input type="radio" name="linguagens" value="css"> CSS
							<input type="radio" name="linguagens" value="javascript"> JavaScript
						</p>
					</div>

					<div>
						<p>
							<label>Quais linguagens você sabe?</label>
							<input type="checkbox" name="linguagens" value="html"> HTML
							<input type="checkbox" name="linguagens" value="css"> CSS
							<input type="checkbox" name="linguagens" value="javascript"> JavaScript
						</p>
					</div>

					<div>
						<label>Qual a sua cor favorita?</label>
						<select>
							<option value="Azul">Azul</option>
							<option value="Verde">Verde</option>
							<option value="Vermelho" selected>Vermelho</option>
						</select>
					</div>

					<div>
						<input type="submit" >
					</div>
					

				</form>

				
				
			</article>


		</section>

		<footer>
			<p>Desenvolvido por Pablo</p>
		</footer>
		
	</body>
</html>
```

### Home page

```
<!DOCTYPE html>

<html lang="pt-br">

<head>

<title>HTML - Pablo</title>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1">

<style>

* {

box-sizing: border-box;

}

  

body {

font-family: Arial, Helvetica, sans-serif;

}

  

/* Style the header */

header {

background-color: #666;

padding: 30px;

text-align: center;

font-size: 35px;

color: white;

}

  

/* Create two columns/boxes that floats next to each other */

nav {

float: left;

width: 30%;

background: #ccc;

padding: 20px;

}

  

/* Style the list inside the menu */

nav ul {

list-style-type: none;

padding: 0;

}

  

article {

float: left;

padding: 20px;

width: 70%;

background-color: #f1f1f1;

}

  

/* Clear floats after the columns */

section::after {

background: #ccc;

content: "";

display: table;

clear: both;

}

  

/* Style the footer */

footer {

background-color: #777;

padding: 10px;

text-align: center;

color: white;

}

  

/* Responsive layout - makes the two columns/boxes stack on top of each other instead of next to each other, on small screens */

@media (max-width: 600px) {

nav, article {

width: 100%;

height: auto;

}

}

</style>

</head>

<body>

  

<header>

<h2>Curso Front-end - HTML</h2>

</header>

  

<section>

  

<nav>

<h3>Aulas</h3>

<ul>

<li><a href="#">Introdução</a></li>

<li><a href="#">Listas e Links</a></li>

<li><a href="#">Formatação de Texto</a></li>

<li><a href="#">Tabelas</a></li>

<li><a href="#">Layouts</a></li>

<li><a href="#">Formulários</a></li>

</ul>

  

<h3>Redes Sociais</h3>

<ul>

<li><a href="#">LinkedIn</li>

<li><a href="#">@ortizao_</li>

</ul>

</nav>

  

<article>

  

<img width="200" src="https://images.unsplash.com/photo-1761839258803-21515f43190c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDF8MHxmZWF0dXJlZC1waG90b3MtZmVlZHwxfHx8ZW58MHx8fHx8" height="200" alt="Pablo Ortiz">

<h2>Pablo Ortiz</h2>

  

<p>Analista de Sistemas</p>

  

</article>

  
  

</section>

  

<footer>

<p>Desenvolvido por Pablo </p>

</footer>

</body>

</html>
```



