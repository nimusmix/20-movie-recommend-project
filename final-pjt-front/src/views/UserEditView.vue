<template>
  <div class="router-view-padding">
    <h1 class="h1">회원정보수정</h1>
    <div class="space"></div>
    <h3 class="h3">내 프로필 사진 변경</h3>
    <div>
      <img v-if="loginUser?.profile_img" :src="`http://127.0.0.1:8000${loginUser?.profile_img}`">
        <img v-else src="@/assets/basic.png" >
        
      <div class="box-file-input">
        <label>
          <input type="file" class="file-input" id="inputGroupFile02" accept="image/*" @change="changeImg" ref="profileImg">
        </label>
          <span class="filename">파일을 선택해주세요.</span>
        </div>

      <div class="input-group mb-3">
        <input type="file" class=""   >
      </div>
      <!-- <div class="main-button" style="max-width:500px">
        <input type="file" value=""  />
      </div> -->
    </div>
    <div class="space"></div>
    <h3  class="h3">좋아하는 장르를 선택해주세요!</h3>
    <div class="button-list">
      <button
        v-for="perference in perferences" :key="perference.genre.id"
        :class="[{'selected': perference.like}, 'main-button']"
        @click="isSelectedGenre(perference)">
        {{ perference.genre_name }}
      </button>
    </div>
    <div class="space"></div>
    <h3 class="h3">사용 중인 OTT를 골라주세요!</h3>
    <div class="button-list">
      <button
        v-for="ott in otts" :key="ott.id"
         :class="[{'selected': ott.like}, 'main-button']" 
          @click="isSelectedOtt(ott)"> 
          {{ ott.name }}
      </button>
    </div>
    

    <div v-if="this.$route.params.signUpFlag === '1'">
      <form @submit.prevent="editInfo('HomeView')">
        <button>건너뛰기</button>
      </form>
      <form @submit.prevent="editInfo('HomeView')">
        <button>가입완료</button>
      </form>
    </div>

    <div v-else>
      <form @submit.prevent="editInfo('ProfileView')">
        <button>수정취소</button>
      </form>
      <form @submit.prevent="editInfo('ProfileView')">
        <button>수정하기</button>
      </form>
    </div>

    <!-- <button @click="editOtt">장르 1</button> -->
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'UserEditView',
  data() {
    return {
        perferences: null,
        otts: null,
        img: null,
    }
  },
  methods: {
    //  선호 오티티 가져오기
    getOtts() {
      this.otts = this.$store.state.otts
      this.otts.forEach((ott)=>ott['like'] = false)
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
          res.data.using_otts.forEach((ott_django)=>{
            this.otts.forEach((ott, index)=>{
              if(ott_django === ott.id){
                this.otts[index].like = true
              }
            })
          })
          this.perferences = res.data
          
          console.log(this.otts)
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
          console.log(res.data)
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
        .then((res) => {
          console.log(res.data)
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
        // .then(() => {
        //   console.log(`${perference.genre} editPreferences 성공!`)
        // })
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
        .then((res) => {
          console.log(res)
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
  },
  mounted(){
    // this.img = this.$store.state.loginUser.profile_img
  }
}
</script>

<style lang="scss">

.box-file-input label{
  display:inline-block;
  background: none;
  color: var(--primary-color);
  background-color: var(--primary-color);
  color:var(--button-live-text-color);
  padding:0px 15px;
  line-height:35px;
  cursor:pointer;
}

.box-file-input label:after{
  content:"파일등록";
}

.box-file-input .file-input{
  display:none;
}

.box-file-input .filename{
  display:inline-block;
  padding-left:10px;
}
</style>