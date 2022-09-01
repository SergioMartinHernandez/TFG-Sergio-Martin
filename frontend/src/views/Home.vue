<template>
  <section class="home_banner_area">
    <div class="banner_inner">
      <div class="container">
        <div class="row">
          <div class="col-lg-7">
            <div class="banner_content">
              <img class="" src="../assets/logoWhite.png" alt="">
              <h4 class="text">Tool For Twitter Data Analysis</h4>
              <div class="d-flex align-items-center">
                <button id="login-button" type="button" class="btn btn-secondary btn-lg btn-block" @click="$router.push('/login')">Log In</button>
                <button id="signup-button" type="button" class="btn btn-lg btn-dark btn-block" @click="$router.push('/signup')">Sign Up</button>
              </div>
            </div>
          </div>
          <div class="col-lg-5">
            <div class="home_right_img">
              <img id="image-home" class="" src="../assets/home-image.png" alt="">
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>


<style scoped>
#login-button {
  margin-top: 20px; 
  margin-right: 20px;
  color: #fff;
  background-color: #343a40;
  border-color: #343a40;
}
#signup-button {
  margin-top: 20px; 
  color: #fff;
  background-color: gray;
  border-color: gray;
}
#image-home {
  display: block;
  max-width: 100%;
  height: auto;
  margin-left: 20px;
} 
.home_banner_area {
    z-index: 1;
    background: url(../assets/home-banner.png) no-repeat top center;
    background-position: center;
    background-size: cover; }
    .home_banner_area .banner_inner {
      width: 100%; }
      .home_banner_area .banner_inner .home_right_img {
        padding-top: 197px; }
        @media (max-width: 1480px) {
          .home_banner_area .banner_inner .home_right_img img {
            max-width: 100%;
            height: auto; } }
        @media (max-width: 991px) {
          .home_banner_area .banner_inner .home_right_img {
            display: none; } }
      .home_banner_area .banner_inner .col-lg-7 {
        vertical-align: middle;
        align-self: center; }
      .home_banner_area .banner_inner .banner_content {
        text-align: left; }
        @media (max-width: 991px) {
          .home_banner_area .banner_inner .banner_content {
            margin-top: 150px; } }
        .home_banner_area .banner_inner .banner_content h3 {
          font-size: 40px;
          margin-bottom: 20px;
          position: relative; }
          .home_banner_area .banner_inner .banner_content h3:after {
            content: '';
            width: 410px;
            height: 2px;
            position: absolute;
            top: 50%;
            left: 23%;
            background: #000000; }
            @media (max-width: 575px) {
              .home_banner_area .banner_inner .banner_content h3:after {
                display: none; } }
        .home_banner_area .banner_inner .banner_content h1 {
          margin-top: 20px;
          font-size: 70px;
          line-height: 60px;
          margin-bottom: 25px; }
          @media (max-width: 1024px) {
            .home_banner_area .banner_inner .banner_content h1 {
              font-size: 60px; } }
          @media (max-width: 767px) {
            .home_banner_area .banner_inner .banner_content h1 {
              font-size: 50px; } }
        .home_banner_area .banner_inner .banner_content h5 {
          font-size: 24px;
          margin-bottom: 35px; }
        .home_banner_area .banner_inner .banner_content .primary_btn {
          margin-right: 20px; }
</style>
