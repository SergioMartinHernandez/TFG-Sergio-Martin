<template>
    <section class="section about-section gray-bg" id="about">
        <div class="container">
            <div class="row align-items-center flex-row-reverse">
                <div class="col-lg-6">
                    <div class="about-text go-to">
                        <h3>About Datter</h3>
                        <p>Datter is a final project for the degree of computer engineering at USAL, it is a tool for the analysis of twitter data that is developed with FastAPI for the backend and VueJS for the frontend.</p>
                        <br/>
                        <h3>About Me</h3>
                        <p>I am Sergio Martín Hernández, a student of computer engineering at the usal, I am 22 years old and this is my first big project. I hope you like the project and that you can get a lot of use out of it.</p>
                        <br/>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="about-logo">
                        <img src="../assets/logo2.png">
                    </div>
                </div>
            </div>
        </div> 
    </section>
</template>

  
<style scoped>
body{
    color: #6F8BA4;
    margin-top:20px;
}
.section {
    padding: 100px 0;
    position: relative;
}
.gray-bg {
    background-color: #f5f5ff;
    height: 100vh;
}
img {
    max-width: 100%;
}
img {
    vertical-align: middle;
    border-style: none;
}
.about-text h3 {
  font-size: 45px;
  font-weight: 700;
  margin: 0 0 6px;
}
@media (max-width: 767px) {
  .about-text h3 {
    font-size: 35px;
  }
}
.about-text p {
  font-size: 18px;
  max-width: 450px;
}
</style>
  