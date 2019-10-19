<template>
	<div id="app" class="d-flex justify-content-center align-items-center">
		<div class="container">
			<div class="row d-flex justify-content-center align-items-center">
				<div class="col-sm-12 col-lg-5 card">
					<div class="card-title">Sign In</div>
					<div class="card-body d-flex justify-content-center align-items-center">
						<form>
							<input type="text" id="login" class="fadeIn second" name="login" placeholder="login" />
							<input type="text" id="password" class="fadeIn third" name="login" placeholder="password" />
							<input type="submit" class="fadeIn fourth" value="Log In" />
						</form>
					</div>
					<div class="card-footer text-center">
						<a href>Create new account</a>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "app"
};
</script>

<style>
#app {
	font-family: "Raleway", sans-serif;
	width: 100vw;
	height: 100vh;
	background: rgb(2, 0, 36);
	background: linear-gradient(
		12deg,
		rgb(59, 59, 177) 10%,
		rgba(0, 212, 255, 1) 100%
	);
}
.card {
	background: white;
	border-radius: 2px;
	min-height: 400px;
}
.card-title {
	padding-top: 20px;
	text-align: center;
	font-size: 2rem;
}

.card-body {
	text-align: center;
}

.card-footer {
	background: none;
}

.card-footer a {
	text-decoration: none;
}

input[type="button"],
input[type="submit"],
input[type="reset"] {
	background-color: #3b3bb1;
	border: none;
	color: white;
	padding: 15px 80px;
	text-align: center;
	text-decoration: none;
	display: inline-block;
	text-transform: uppercase;
	font-size: 13px;
	-webkit-box-shadow: 0 10px 30px 0 rgba(95, 186, 233, 0.4);
	box-shadow: 0 10px 30px 0 rgba(95, 186, 233, 0.4);
	-webkit-border-radius: 5px 5px 5px 5px;
	border-radius: 5px 5px 5px 5px;
	margin: 40px 20px 40px 20px;
	-webkit-transition: all 0.3s ease-in-out;
	-moz-transition: all 0.3s ease-in-out;
	-ms-transition: all 0.3s ease-in-out;
	-o-transition: all 0.3s ease-in-out;
	transition: all 0.3s ease-in-out;
}

input[type="button"]:hover,
input[type="submit"]:hover,
input[type="reset"]:hover {
	background-color: #39ace7;
}

input[type="button"]:active,
input[type="submit"]:active,
input[type="reset"]:active {
	-moz-transform: scale(0.95);
	-webkit-transform: scale(0.95);
	-o-transform: scale(0.95);
	-ms-transform: scale(0.95);
	transform: scale(0.95);
}

input[type="text"] {
	background-color: #f6f6f6;
	border: none;
	color: #0d0d0d;
	padding: 15px 32px;
	text-align: center;
	text-decoration: none;
	display: inline-block;
	font-size: 16px;
	margin: 5px;
	width: 85%;
	border: 2px solid #f6f6f6;
	-webkit-transition: all 0.5s ease-in-out;
	-moz-transition: all 0.5s ease-in-out;
	-ms-transition: all 0.5s ease-in-out;
	-o-transition: all 0.5s ease-in-out;
	transition: all 0.5s ease-in-out;
	-webkit-border-radius: 5px 5px 5px 5px;
	border-radius: 5px 5px 5px 5px;
}

input[type="text"]:focus {
	background-color: #fff;
	border-bottom: 2px solid #3b3bb1;
}

input[type="text"]:placeholder {
	color: #cccccc;
}
</style>
