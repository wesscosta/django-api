from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from gtts import gTTS
import os

class TextToAudioView(APIView):
    def post(self, request):
        from .serializers import TextToAudioSerializer
        serializer = TextToAudioSerializer(data=request.data)
        
        if serializer.is_valid():
            text = serializer.validated_data['text']
            language = serializer.validated_data.get('language', 'pt')  # Português por padrão


            try:
                # Converter texto em áudio
                tts = gTTS(text=text, lang=language)
                file_path = "audio_output.mp3"
                tts.save(file_path)

                # Retornar o caminho do arquivo
                return Response({
                    'message': 'Audio generated successfully!',
                    'file_url': request.build_absolute_uri(f'/media/{file_path}')
                }, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
