<template>
  <div class="router-view-padding">
    <h1 class="h1" v-if="this.$route.params.signUpFlag === '1'">선택 정보 입력</h1>
    <h1 class="h1" v-else>회원정보수정</h1>
    <div class="space"></div>

    <h3 class="h3">내 프로필 사진</h3>
    <div class="img-select-box">
      <div>
        <img class="img-circle-80" v-if="loginUser?.profile_img" :src="`${$store.state.API_URL}${loginUser?.profile_img}`">
        <img class="img-circle-80" v-else src="@/assets/basic.png" >
      </div>
      
      <div class="box-file-input" style="margin-top:8px">
        <label for="inputGroupFile02" class="cicle-lr">
          <input type="file" class="file-input cicle-lr" id="inputGroupFile02" accept="image/*" @change="changeImg" ref="profileImg">
        </label>
      </div>
    </div>
      

    <div class="space"></div>
    <h3 class="h3">좋아하는 장르를 선택해주세요.</h3>
    <div class="button-list" v-if="perferences">
      <button
        v-for="perference in perferences" :key="perference?.genre?.id"
        :class="[{'selected': perference?.like}, 'main-button']"
        @click="isSelectedGenre(perference)">
        {{ perference?.genre_name }}
      </button>
    </div>
    <div class="space"></div>
    <h3 class="h3">사용 중인 OTT를 골라주세요.</h3>
    <div class="button-list">
      <button
        v-for="ott in otts" :key="ott?.id"
         :class="[{'selected': ott?.like}, 'main-button']" 
          @click="isSelectedOtt(ott)"> 
          {{ ott.kor }}
      </button>
    </div>
    
    <div class="space"></div>
    <div class="cusor-pointer">
    <div v-if="this.$route.params.signUpFlag === '1'"  @click="editInfo('HomeView')">
      <h2 class="h2" style="color:#FF715E;">가입완료
      <svg style="display:inline-block; color:#FF715E; text-decoration:underline;" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 28 28" fill="none">
        <path d="M8.91016 19.9201L15.4302 13.4001C16.2002 12.6301 16.2002 11.3701 15.4302 10.6001L8.91016 4.08008" stroke="#FF715E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
      </svg></h2>
    </div>

    <div v-else @click="editInfo('ProfileView')">
      <h2 class="h2" style="color:#FF715E; text-decoration:underline;">수정하기
      <svg style="display:inline-block" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 28 28" fill="none">
        <path d="M8.91016 19.9201L15.4302 13.4001C16.2002 12.6301 16.2002 11.3701 15.4302 10.6001L8.91016 4.08008" stroke="#FF715E" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
      </svg></h2>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'UserEditView',
  data() {
    return {
      perferences: null,
      otts: [
        {
          id: 97,
          name: 'watcha',
          kor: '왓챠',
          like: false,
        },
        {
          id: 356,
          name: 'waave',
          kor: '웨이브',
          like: false,
        },
        {
          id: 337,
          name: 'disney',
          kor: '디즈니',
          like: false,
        },
        {
          id: 8,
          name: 'netflix',
          kor: '넷플릭스',
          like: false,
        },    
      ],
      img: null,
      recommendBaseList: [
        {
          name: 'similar',
          url: 'api/v1/recommend/similar',
        },
        {
          name: 'latent',
          url: 'api/v1/recommend/latent',
        },
        {
          name: 'preference',
          url: 'api/v1/recommend/preference',
        }
      ],
    }
  },
  methods: {
    //  선호 오티티 가져오기
    getOtts() {
      axios({
        method: 'get',
        url: `${this.$store.state.API_URL}/api/v3/accounts/otts/`,
        headers: {
            Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then((res) => {
          console.log('otts 성공!')
          //this.otts를 돌면서, 안에 있는지 파악해서 바꿔준다.
          res.data.using_otts.forEach((ott_django) => {
            this.otts.forEach((ott, index) => {
              if (ott_django === ott.id) {
                this.otts[index].like = true
              }
            })
          })
        })
        .catch((err) => {
          console.log('otts 실패!')
          console.log(err)
        })
    },
    // 선호 장르를 받아온다.
    getPerferences() {
      axios({
        method: 'get',
        url: `${this.$store.state.API_URL}/api/v3/accounts/perferences/`,
        headers: {
            Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then((res) => {
          console.log('1 actions의 editInfo 성공!')
          this.perferences = res.data
        })
        .catch((err) => {
          console.log('actions의 editInfo 실패!')
          console.log(err)
        })
    },
    changeImg() {
      this.getImg = this.$refs.profileImg.files[0]
      this.editProfileImg()
    },
    editProfileImg() {
      axios({
        method: 'put',
        url: `${this.$store.state.API_URL}/api/v3/accounts/edit-profile-img/`,
        data: {
          'profile_img': this.getImg,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
          'Content-Type': 'multipart/form-data',
        },
      })
        .then(() => {
          this.$store.dispatch('getLoginUser')
        })
        .catch((err) => {
          console.log(err)
        })
        
    },
    // 선호 장르 수정
    editPreferences(perference) {
      axios({
        method: 'put',
        url: `${this.$store.state.API_URL}/api/v3/accounts/edit-perferences-like/${perference.genre}/`,
        data: {
            'like': perference.like,
        },
        headers: {
            Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then(() => {
          console.log(`${perference.genre} editPreferences 성공!`)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    editOtts(ott){
      axios({
        method: 'put',
        url: `${this.$store.state.API_URL}/api/v3/accounts/edit-otts/${ott.id}/`,
        headers: {
            Authorization: `Token ${this.$store.state.token}`
        },
      })
        .catch((err) => {
          console.log(err)
        })
    },
    // 회원 정보 수정
    editInfo(nextPage) {
      if (nextPage === 'HomeView') {
        this.$router.push({ name: nextPage })
      } else if (nextPage === 'ProfileView') {
        this.$router.push({ name: nextPage, params: { username: this.username } })
      }
    },
    genreCheck(event) {
      event.target.innerText
    },
    isSelectedGenre(perference) {
      const idx = this.perferences.indexOf(perference)
      this.perferences[idx].like = !this.perferences[idx].like
      this.editPreferences(perference)
    },
    isSelectedOtt(ott) {
      const idx = this.otts.indexOf(ott)
      this.otts[idx].like = !this.otts[idx].like
      this.editOtts(ott)
    },
  },
  computed:{
    username() {
      return this.$store.state.username
    },
    loginUser() {
      return this.$store.state.loginUser
    }
  },
  created() {
    this.getPerferences()
    this.getOtts()
    for (const recommendObj of this.recommendBaseList) {
      this.$store.dispatch('getRecommend', recommendObj)
    }
  },
}
</script>

<style lang="scss">
  .img-select-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 90px;
  }

  .box-file-input label{
    display:inline-block;
    background: none;
    background-color: var(--primary-color);
    color:var(--button-live-text-color);
    padding:0px 15px;
    line-height:35px;
    cursor:pointer;
  }

  .box-file-input label:after{
    content:"사진 변경";
  }

  .box-file-input .file-input{
    display:none;
  }
</style>