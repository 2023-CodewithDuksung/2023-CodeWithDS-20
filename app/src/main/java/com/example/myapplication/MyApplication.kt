package com.example.myapplication

import android.app.Application
import androidx.multidex.MultiDexApplication
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.ktx.auth
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.ktx.Firebase

class MyApplication: MultiDexApplication() {
    companion object{
        lateinit var auth : FirebaseAuth
        var email:String? = null
        fun checkAuth(): Boolean{
            var currentuser = auth.currentUser
            return currentuser?.let{
                email = currentuser.email
                if(currentuser.isEmailVerified) true
                else false
            } ?: false
        }
    }

    override fun onCreate() {
        super.onCreate()
        auth = Firebase.auth
    }
}