from django.shortcuts import render

import speech_recognition as sr
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AudioFile
from .serializers import AudioFileSerializer

class AudioTranscriptionView(APIView):
    def post(self, request):
        # Serializa o arquivo enviado
        serializer = AudioFileSerializer(data=request.data)
        if serializer.is_valid():
            audio_file = serializer.save()
            
            # Processa o áudio e realiza a transcrição
            recognizer = sr.Recognizer()
            audio_path = audio_file.audio.path
            try:
                with sr.AudioFile(audio_path) as source:
                    audio_data = recognizer.record(source)
                    transcription = recognizer.recognize_google(audio_data, language='pt-BR')
                    audio_file.transcription = transcription
                    audio_file.save()
                return Response(AudioFileSerializer(audio_file).data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
