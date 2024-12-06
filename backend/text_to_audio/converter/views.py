from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from gtts import gTTS
import os
from django.conf import settings

class TextToAudioView(APIView):
    def post(self, request):
        from .serializers import TextToAudioSerializer
        serializer = TextToAudioSerializer(data=request.data)
        
        if serializer.is_valid():
            text = serializer.validated_data['text']
            language = serializer.validated_data.get('language', 'pt')  # Português por padrão

            try:
                # Configurar o caminho do arquivo para o diretório de mídia
                file_path = os.path.join(settings.MEDIA_ROOT, "audio_output.mp3")

                # Converter texto em áudio e salvar no diretório configurado
                tts = gTTS(text=text, lang=language)
                tts.save(file_path)

                # Construir a URL para o arquivo salvo
                file_url = request.build_absolute_uri(f'{settings.MEDIA_URL}audio_output.mp3')

                return Response({
                    'message': 'Audio generated successfully!',
                    'file_url': file_url
                }, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
