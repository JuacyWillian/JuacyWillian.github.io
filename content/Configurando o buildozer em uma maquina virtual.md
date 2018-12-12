Title: Configurando o buildozer em uma maquina virtual
Date: 2016-12-03 10:20
Category: Python
Tags: Kivy, Buildozer
Authors: Juacy Willian
Lang: pt-br
Summary: Neste artigo eu ensino como prepoarar o ambiente da uma maquina virtual e instalar o buildozer para empacotar os seus aplicativos kivy em instaladores android (.apk).


### Baixar a iso do lubuntu 16.04 32bit e instalar em uma maquina virtual

Eu criei uma VM com:

* RAM 2Gb
* HD 24Gb (criei com tanto espaço porque não gosto de ficar limitado e o meu hd tem 1Tb)
* Video 128Mb

### Atualizando a VirtualMachine:
    sudo apt update && sudo apt upgrade -y

##### Instalando o PyEnv
Como eu não gosto de misturar o python do sistema com o dos meus projetos, por motivos de incompatibilade e estabilidade do sistema, eu prefiro criar ambientes virtuais com o python para cada projeto, e para isso usaremos o PyEnv.

Seguindo o guia do mestre Henrique Bastos para instalar o pyenv e configurá-lo da melhor maneira possível, iremos utilizar alguns comandos... [Link para o quia!](https://medium.com/welcome-to-the-django/guia-definitivo-para-organizar-meu-ambiente-python-a16e2479b753)

Instalação do pyenv, pyenv-virtualenv e pyenv-virtualenvwrapper:

**instalando as dependências do pyenv:**

```bash
$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev\
 libncursesw5-dev xz-utils tk-dev git
```

**instalando o pyenv:**

```bash
$ curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
```

**instalando o pyenv-virtualenvwrapper:**

```bash
$ git clone https://github.com/yyuu/pyenv-virtualenvwrapper.git ~/.pyenv/plugins/pyenv-virtualenvwrapper
```

Agora que o pyenv está instalado, vamos precisar editar o arquivo .bashrc, para isso abra o arquivo ~/.bashrc com o seu editor favorito e não mexa em nada por enquanto, vá até o final do arquivo e digite as seguintes linhas:

```sh
export PATH=~/.pyenv/bin:$PATH
export WORKON_HOME=~/.ve
export PROJECT_HOME=~/workspace

eval "$(pyenv init -)"
#pyenv virtualenvwrapper_lazy
```
Salve as mudanças e feche o editor, agora vamos criar os diretórios que mencionamos acima, no terminal digite:

```bash
mkdir ~/.ve
mkdir ~/workspace
```

Feito isso vamos criar os ambientes base do pyenv.

##### Criando os Ambientes Base:

vamos criar os ambientes que o pyenv vai usar como base para algumas bibliotecas em comum com os nossos projetos. No terminal digite:

```bash
$ pyenv install 3.6.0 && pyenv install 2.7.13
```

Isso vai demorar um pouquinho, então aproveita para beber uma água ou ir ao banheiro. Quando terminar, vamos instalar algumas bibliotecas auxiliares e configurá-las adequadamente. Use os comandos abaixo:

``` bash
$ pyenv virtualenv 3.6.0 jupyter3
$ pyenv virtualenv 3.6.0 tools3
$ pyenv virtualenv 2.7.13 ipython2
$ pyenv virtualenv 2.7.13 tools2
```
O comando acima irá criar 4 ambientes virtuais. Agora iremos configurar cada um, com os seguintes comandos:

```bash
$ pyenv activate jupyter3
$ pip install jupyter
$ python -m ipykernel install --user
$ pyenv deactivate

$ pyenv activate ipython2
$ pip install ipykernel
$ python -m ipykernel install --user
$ pyenv deactivate

$ pyenv activate tools3
$ pip install youtube-dl gnucash-to-beancount rows
$ pyenv deactivate

$ pyenv activate tools2
$ pip install rename s3cmd fabric mercurial

$ pyenv global 3.6.0 2.7.13 jupyter3 ipython2 tools3 tools2
```

Ótimo, ambientes criados e configurados, agora falta só mais uma coisinha e para isso precisamos criar um profile padrão do iPython e instalar um arquivo de inicialização que criei para fazer essa mágica, então digite o seguinte comando no terminal:

```bash
$ ipython profile create
$ curl -L http://hbn.link/hb-ipython-startup-script > ~/.ipython/profile_default/startup/00-venv-sitepackages.py
```

Ufa...  finalmente terminamos de configurar o pyenv. Agora abra novamente o .bashrc  e vamos agora retirar a cerquilha da ultima linha que escrevemos.

```bash
#pyenv virtualenvwrapper_lazy
```

vai ficar assim

```bash
pyenv virtualenvwrapper_lazy
```

Feito isso, feche o terminal e abra novamente. Você vai perceber que serão baixados alguns arquivos do virtualenwrapper que estavam faltando, apenas espere e pronto! Já podemos criar o ambiente virtual do nosso projeto.

##### Criando um Ambiente Virtual

Para criarmos um ambiente virtual para o nosso projeto com python2 para rodar o Buildozer vamos digitar o comando abaixo no terminal:

```bash
$ mkproject -p python2 kv27
```

Lembrando que o python3 é o padrão, então se quiser criar um ambiente virtual com python3 basta digitar:

```bash
$ mkproject [nome_do_ambiente]
```

Esses comandos acima criarão um ambiente virtual no diretório **~/.ve/nome_do_projeto** e um diretório em **~/workspace/nome_do_projeto** para os arquivos do projeto, e mudaŕa o diretório atual para o mesmo.

##### Ativando o ambiente virtual e instalando o kivy  e o buildozer

para ativar o ambiente virtual basta digitar:

```bash
$ workon nome_do_projeto

para desativar digite:

```bash
$ deactivate
```

**vamos instalar o kivy e o buildozer**
vamos instalar o kivy no ambiente do nosso projeto, para isso precisamos ativar o ambiente do projeto com **workon nome_do_projeto**:
uma vez ativo o terminal mudará e ficará mais ou menos assim:

    (nome_do_projeto)user@maquina:~/workspace/nome_do_projeto$

Indicando que voce está com o ambiente ativo em **(nome_do_ambiente)** e no diretorio do projeto em **~/workspace/nome_do_projeto$**

**Instalando as dependencias do kivy**

    sudo apt-get install -y python-pip build-essential git python python-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev


```bash
$ pip install cython
```

**Instalando o Kivy, finalmente**


```bash
$ pip install kivy
```

**Instalando as dependencias do buildozer**

```bash
$ sudo apt-get install build-essential ccache git libncurses5 libstdc++6 libgtk2.0-0 libpangox-1.0-0 libpangoxft-1.0-0 libidn11 python2.7 python2.7-dev openjdk-8-jdk unzip zlib1g-dev zlib1g
```

**Instalando o buildozer**


```bash
$ pip install buildozer
```

#### Dicas

O buildozer aqui não funcionou com o python3, apenas com o python 2, então eu sugiro que usem o py2 para desenvolver o seu app ou escreva codigo compativel com python 2 e 3
