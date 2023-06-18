package com.example.testapplication.service

import com.example.testapplication.model.request.creatroomrequest
import com.example.testapplication.model.request.loginrequest
import com.example.testapplication.model.request.searchroomrequest
import com.example.testapplication.model.request.signuprequest
import com.example.testapplication.model.response.*
import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST

interface SignService {

    @POST("signup/")
    fun signup(
        @Body request: signuprequest
    ): Call<signupresponse>

    @POST("login/")
    fun signin(
        @Body request: loginrequest
    ): Call<loginresponse>
}

interface CreateRoomService{
    @POST("roomcreate/")
    fun roomcreate(
        @Body request: creatroomrequest
    ): Call<createroomresponse>
}

interface SearchRoomService{
    @POST("roomsearch/")
    fun roomsearch(
        @Body request: searchroomrequest
    ): Call<searchroomresponse>
}

interface RoomlistService{
    @GET("getroomlist/")
    fun roomlist(
    ): Call<getroomlistresponse>
}