<h1>Script na Fase de Reconhecimento em Python para Pentest</h1>

<h2>Descrição</h2>
O projeto consiste em desenvolver um script que faz o reconhecimento de arquivos e diretórios em uma aplicação WEB, no caso utilizando ips para verificação.
<br />


<h2>Linguagens e Serviços utilizados/VMS:</h2>

- <b>Visual Studio Code</b> 
- <b>Python3</b>
- <b>Kali Linux </b>
- <b>Metasploitable </b>
- <b>Oracle VirtualBox </b>

<h2>Ambientes Usados </h2>

- <b>Windows 11</b>
- <b>Kali Linux(Debian 64-bits) </b>
- <b>Metasploitable(Linux x2.6 32-bits) </b>

<h2>Andamento da Aplicação:</h2>

<p align="center">
Primeiro precisamos usar bibliotecas como Argeparse e Socket: <br/>
<img src="https://i.imgur.com/Y5WY3zH.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Logo definindo os argumentos com arquivos locais para realizar a força bruta:  <br/>
<img src="https://i.imgur.com/ItMcONE.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Utilizando os argumentos: <br/>
<img src="https://i.imgur.com/Q6Ko5ca.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Criando a função que realizará a lista dos sub domínios:  <br/>
<img src="https://i.imgur.com/d4lPJ4l.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Script realizado com sucesso na VM Metasploitable:  <br/>
<img src="https://i.imgur.com/LR1L0f6.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>

