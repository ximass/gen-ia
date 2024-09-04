<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Events\MessageSent;

class MessageController extends Controller
{
    public function send(Request $request)
    {
        $userMessage = $request->input('message');
        
        $command = escapeshellcmd('python C:\projetos\gen-ia\scripts\test3.py ' . escapeshellarg($userMessage));
        $output  = shell_exec($command);
        
        if ($output === null) {
            return response()->json(['success' => false, 'message' => 'Falha ao consultar o ChatGPT.']);
        }

        event(new MessageSent('Pergunta: ' . $request->input('message')));

        broadcast(new MessageSent('Resposta: ' . json_decode($output)->choices[0]->message));
        
        return response()->json(['success' => true, 'message' => 'Mensagem enviada com sucesso!']);
    }
}


?>