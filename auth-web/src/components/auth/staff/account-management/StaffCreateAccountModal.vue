<template>
  <v-container class="pa-0 create-account-modal" data-test="create-account-modal">
    <ModalDialog
      ref="createAccountDialog"
      title="Create Account"
      dialog-class="create-account-dialog"
      max-width="660"
      :show-icon="false"
      :showCloseIcon="true"
      data-test="modal-create-account"
    >
    <template v-slot:title>
      <h2 class="text-h2 font-weight-bold pl-3 ">Create Account</h2>
    </template>
    <template v-slot:text>
    <v-radio-group
      hide-details
      class="font font-weight-bold mt-1 pl-3"
      v-model="selctedAccount"
      data-test="radio-selctedAccount"
    >
      <v-radio :value="accountTypes.DIRECTOR_SEARCH" data-test="radio-director">
        <template v-slot:label>
          <div class="font font-weight-bold text--primary">Director Search Account</div>
        </template>
     </v-radio>
      <p class="ml-8 mb-11">Create an account for director search account for directors who is a member of the board of a company</p>
      <v-radio :value="accountTypes.GOVM_BUSINESS"  data-test="radio-government">
        <template v-slot:label>
          <div class="font font-weight-bold text--primary">BC Provincial Government Ministry/Employee</div>
        </template>
      </v-radio>
      <p class="ml-8 mb-7">Send an invite to GOVM business type account for different ministries</p>

    </v-radio-group>
      </template>
      <template v-slot:actions class="justify-end">
        <v-btn large color="primary" @click="createAccount()" data-test="btn-continue" class="font font-weight-bold px-3">
        Continue
        </v-btn>
        <v-btn large color="default" @click="close()" data-test="btn-cancel" class="font font-weight-bold px-3 mr-1 ml-5 ">
          Cancel
        </v-btn>
      </template>
    </ModalDialog>

  </v-container>
</template>

<script lang="ts">
import { Component, Emit, Vue } from 'vue-property-decorator'
import { Pages, StaffCreateAccountsTypes } from '@/util/constants'
import ModalDialog from '@/components/auth/common/ModalDialog.vue'

@Component({
  components: {
    ModalDialog
  }
})
export default class StaffCreateAccountModal extends Vue {
  private selctedAccount: string = StaffCreateAccountsTypes.DIRECTOR_SEARCH
  public accountTypes: any = StaffCreateAccountsTypes

  $refs: {
    createAccountDialog: ModalDialog
  }

  public open () {
    this.$refs.createAccountDialog.open()
  }

  public close () {
    this.$refs.createAccountDialog.close()
  }

  createAccount () {
    if (this.selctedAccount === StaffCreateAccountsTypes.DIRECTOR_SEARCH) {
      this.$router.push({ path: `/${Pages.STAFF_SETUP_ACCOUNT}` })
    } else {
      this.$router.push({ path: `${Pages.STAFF_GOVM_SETUP_ACCOUNT}` })
    }
  }
}
</script>
<style lang="scss" >
.create-account-dialog{
    .v-card__actions{
        justify-content: flex-end;
    }

}
</style>
