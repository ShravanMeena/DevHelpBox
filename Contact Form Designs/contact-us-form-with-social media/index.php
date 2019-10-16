<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title> Contact Form </title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,500,600,700,800,900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="layer"></div>


<div class="page-content">

    <div class="container">

        <div class="row">

            <div class="col-sm-5">

                <div class="contact-form shadow">

                    <h2 class="heading-sm">Send us your message</h2>
                    <p class="sub-title-sm mb-4">Fill up the form and instantly send us your queries or feedback</p>

                    <div class="row">
                        <div class="col-sm-6">
                            <div class="form-group">
                                <input type="text" class="form-control" name="name" placeholder="Full Name">
                                <label for="name"><i class="far fa-user"></i></label>
                            </div>
                        </div>
                        <div class="col-sm-6">
                            <div class="form-group">
                                <input type="tel" class="form-control" name="phone" placeholder="Phone">
                                <label for="phone"><i class="fas fa-phone"></i></label>
                            </div>
                        </div>
                        <div class="col-sm-12">
                            <div class="form-group">
                                <textarea type="text" class="form-control" name="message" placeholder="Message"></textarea>
                                <label for="message"><i class="far fa-envelope"></i></label>
                            </div>
                        </div>
                        <div class="col-sm-8"></div>
                        <div class="col-sm-4 text-right">
                            <button type="submit" class="btn-ajax"><i class="fas fa-arrow-right"></i></button>
                        </div>
                    </div>
                </div>


                <div class="social mt-5">
                    <h2 class="heading-sm">
                        <span><i class="fas fa-share-alt"></i></span>
                        Be Social
                    </h2>
                    <p class="sub-title-sm mb-4">Get notified quickly to our latest updates and events. Subscribe to our social channels</p>

                    <div class="social-links">
                        <a href="#" class="link facebook" data-toggle="tooltip" data-placement="bottom" title="Facebook">
                            <i class="fab fa-facebook-f"></i>
                        </a>

                        <a href="#" class="link twitter" data-toggle="tooltip" data-placement="bottom" title="Twitter">
                            <i class="fab fa-twitter"></i>
                        </a>

                        <a href="#" class="link linkedin" data-toggle="tooltip" data-placement="bottom" title="LinkedIn">
                            <i class="fab fa-linkedin-in"></i>
                        </a>

                        <a href="#" class="link youtube" data-toggle="tooltip" data-placement="bottom" title="Youtube">
                            <i class="fab fa-youtube"></i>
                        </a>


                        <a href="#" class="link whatsapp" data-toggle="tooltip" data-placement="bottom" title="WhatsApp">
                            <i class="fab fa-whatsapp"></i>
                        </a>
                    </div>

                </div>

            </div>

        </div>

    </div>

</div>

<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>


</body>
</html>
